#!/usr/bin/env python3

import file
import web_pages
import utility
import argparse
import sys
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    description = """Reads in a file with a list of URLs, collects title tags
    and meta descriptions of these websites and writes this data into a csv
    file. Additionally the quality and length can be checked"""
    parser = argparse.ArgumentParser(description)
    parser.add_argument('-i', '--input', dest='input_file', action='store',
                        required=True,
                        help='Specify input file or a single url')
    parser.add_argument('-c', '--check', action='store_true',
                        help='Flag to indicate whether data should be checked')
    parser.add_argument('-p', '--pretty', action='store_true',
                        help='Flag to indicate whether data should be\
                        prettified, i.e. Removes all newlines, tabs, returns\
                        and spaces at beginning and ending of data.')

    args = parser.parse_args()
    urls = file.get_lines_from_file(args.input_file)
    webpage_checker = MetaDataChecker(urls)
    webpage_checker.gather_webpage_data()

    if args.check:
        webpage_checker.check_webpage_data()

    if args.pretty:
        webpage_checker.prettify_webpage_data()

    webpage_checker.write_webpage_data_file()

    return 0


class MetaDataChecker(object):
    MAX_TITLE_LENGTH = 69
    MAX_DESCR_LENGTH = 160

    def __init__(self, urls):
        self.urls = urls
        self.pages = []
        self.headers = ['Title Tags', 'Meta Descriptions', 'URLs']

    def gather_webpage_data(self):
        """Gathers data of all web pages specified in the url list"""
        print("Getting web page data:")
        for url in self.urls:
            utility.show_progress()
            page = urlopen(url).read()
            web_page = web_pages.WebPage(url)
            web_page.setup_from_soup(BeautifulSoup(page))
            self.pages.append(web_page)

        print('')
        print("All data received!")

    def write_webpage_data_file(self, file_name='output.csv'):
        """Writes all gathered web page datas into a csv file"""
        config = ['title', 'description', 'url', 'comment']
        with open(file_name, 'w', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(self.headers)
            for web_page in self.pages:
                writer.writerow(web_page.get_printable_list(config))

    def prettify_webpage_data(self):
        """Prettifies data of web pages, i.e. removes newlines, tabs and spaces\
        at end and beginning of file"""
        for data in self.pages:
            data.prettify_data()

    def check_webpage_data(self):
        """Check title tag and meta description lengths"""
        no_errors = 0
        for web_page in self.pages:
            if web_page.has_title():
                if len(web_page.title_tag) > self.MAX_TITLE_LENGTH:
                    comment = "Title tag is too long (%d). It should be %d" %\
                        (len(web_page.title_tag), self.MAX_TITLE_LENGTH)
                    web_page.add_comment(comment)
                    no_errors += 1
            else:
                web_page.add_comment("No title tag!")
                no_errors += 1
            if web_page.has_description():
                if len(web_page.meta_description) > self.MAX_DESCR_LENGTH:
                    comment = "Meta description is too long (%d). It should be %d" %\
                        (len(web_page.meta_description), self.MAX_DESCR_LENGTH)
                    web_page.add_comment(comment)
                    no_errors += 1
            else:
                web_page.add_comment("No meta description!")
                no_errors += 1

        if no_errors > 0:
            error_msg = "==> Found %d Errors in meta data" % no_errors
            print(error_msg)
        else:
            print("==> No Errors found!")


if __name__ == '__main__':
    sys.exit(main())
