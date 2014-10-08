#!/usr/bin/env python3

import file
import web_pages
import utility
import argparse
import sys
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
        # MetaDataChecker.check_wepage_data()
        pass

    if args.pretty:
        # MataDataChecker.prettify_webpage_data()
        pass

    # MeatDataChecker.write_webpage_data_file()

    return 0


class MetaDataChecker(object):
    def __init__(self, urls):
        self.urls = urls
        self.pages = []

    def gather_webpage_data(self):
        """Gathers data of all web pages specified in the url list"""
        print("Getting web page data:")
        for url in self.urls:
            utility.show_progress()
            page = urlopen(url).read()
            web_page = web_pages.WebPage(BeautifulSoup(page))
            page_data = []
            page_data.append(web_page.get_title_tag())
            page_data.append(web_page.get_meta_description())
            page_data.append(url)
            self.pages.append(page_data)

            print('')
            print("All data received!")


if __name__ == '__main__':
    sys.exit(main())
