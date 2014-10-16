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
    description = """Reads in a file with a list of URLs, collects all html
    headers of these websites, counts h1-h6 headers and writes this data into
    a csv file."""
    parser = argparse.ArgumentParser(description)
    parser.add_argument('-i', '--input', dest='input_file', action='store',
                        required=True,
                        help='Specify input file or a single url')
    parser.add_argument('-c', '--count', action='store_true',
                        help='Flag to indicate whether the html headers should\
                        be counted')
    parser.add_argument('-p', '--pretty', action='store_true',
                        help='Flag to indicate whether data should be\
                        prettified, i.e. Removes all newlines, tabs, returns\
                        and spaces at beginning and ending of data.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Flag to indicate whether additional information\
                        should be printed')

    args = parser.parse_args()
    urls = file.get_lines_from_file(args.input_file)
    webpage_checker = HeaderChecker(urls)
    webpage_checker.gather_webpage_data()

    is_verbose = False
    if args.verbose:
        is_verbose = True

    if args.pretty:
        webpage_checker.prettify_webpage_data()

    if args.count:
        webpage_checker.write_numbers_of_headers_file(is_verbose)
    else:
        webpage_checker.write_webpage_data_file(is_verbose)

    return 0


class HeaderChecker(object):
    def __init__(self, urls):
        self.urls = urls
        self.pages = []
        self.headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'URLs']

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

    def write_webpage_data_file(self, with_comments, file_name='headers.csv'):
        """Writes all gathered web page datas into a csv file"""
        with open(file_name, 'w', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(self.headers)
            for web_page in self.pages:
                writer.writerow(
                    web_page.get_printable_html_headers(with_comments))

    def write_numbers_of_headers_file(self, with_comments,
                                      file_name='header_numbers.csv'):
        """Counts h1 - h6 headers on the web pages"""
        with open(file_name, 'w', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(self.headers)
            for web_page in self.pages:
                writer.writerow(
                    web_page.get_printable_header_numbers(with_comments))

    def prettify_webpage_data(self):
        """Prettifies data of web pages, i.e. removes newlines, tabs and spaces\
        at end and beginning of file"""
        for data in self.pages:
            data.prettify_data()


if __name__ == '__main__':
    sys.exit(main())
