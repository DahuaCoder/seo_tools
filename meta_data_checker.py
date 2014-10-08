#!/usr/bin/env python3

import file
import argparse
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    description = """Reads in a file with a list of URLs, collects title tags and meta
    descriptions of these websites and writes this data into a csv file. Additionally the quality
    and length can be checked"""
    parser = argparse.ArgumentParser(description)
    parser.add_argument('-i', '--input', dest='input_file', action='store', required=True,
                        help='Specify input file or a single url')
    parser.add_argument('-c', '--check', action='store_true',
                        help='Flag to indicate whether data should be checked')

    args = parser.parse_args()
    input_file = file.File(args.input_file)

    return 0


class MetaDataChecker(object):
    def __init__(self, urls):
        self.web_pages = urls

    def get_web_pages(self, urls):
        """Gets data from specified urls"""


def get_metadata(urls):
    h1_titles = []
    titles = []
    descriptions = []
    print("Getting websites ", end='')
    for remote_url in urls:
        show_progress()
        page = urlopen(remote_url).read()
        soup = BeautifulSoup(page)
        h1 = soup.h1.string
        h1_titles.append(make_pretty(h1))
        title_tag = soup.title.string
        titles.append(make_pretty(title_tag))
        soup_meta_desc = soup.findAll('meta', attrs={"name": "description"})
        descr = soup_meta_desc[0]['content']
        descriptions.append(make_pretty(descr))

    print('')
    print('')
    print("All data received!")

    return((h1_titles, titles, descriptions))




if __name__ == '__main__':
    sys.exit(main())
