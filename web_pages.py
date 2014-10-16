#!/usr/bin/env python3

import file
import sys
from bs4 import BeautifulSoup


class WebPage(object):
    def __init__(self, url):
        self.url = url
        self.comment = None

    def setup_from_soup(self, soup):
        """Reads all required data from BeautifulSoup object and initializes web
        page"""
        if not isinstance(soup, BeautifulSoup):
            raise TypeError("bar must be set to an integer")
        self.title_tag = soup.title.string
        self.meta_description = None
        soup_meta_desc = soup.findAll('meta',
                                      attrs={"name": "description"})
        if soup_meta_desc:
            self.meta_description = soup_meta_desc[0]['content']

        self.h1_headers = self._get_html_headers(soup, 'h1')
        self.h2_headers = self._get_html_headers(soup, 'h2')
        self.h3_headers = self._get_html_headers(soup, 'h3')
        self.h4_headers = self._get_html_headers(soup, 'h4')
        self.h5_headers = self._get_html_headers(soup, 'h5')
        self.h6_headers = self._get_html_headers(soup, 'h6')

    def has_title(self):
        """Returns true if web page has a title tag"""
        if self.title_tag:
            return True
        else:
            return False

    def has_description(self):
        """Return true if web page has a meta description"""
        if self.meta_description:
            return True
        else:
            return False

    def get_printable_meta_data(self):
        """Returns a list containing all the meta data, url and comment in a
        printable format"""
        print_data = [self.title_tag, self.meta_description, self.url,
                      self.comment]
        return print_data

    def get_printable_html_headers(self):
        """Returns a list containing all the html headers, url and comment in a
        printable format"""
        print_data = [self.h1_headers, self.h2_headers, self.h3_headers,
                      self.h4_headers, self.h5_headers, self.h6_headers,
                      self.url, self.comment]
        return print_data

    def get_printable_header_numbers(self):
        """Returns a list containing all the numbers of html headers, url and
        comment in a printable format"""
        print_data = [len(self.h1_headers), len(self.h2_headers),
                      len(self.h3_headers), len(self.h4_headers),
                      len(self.h5_headers), len(self.h6_headers),
                      self.url, self.comment]
        return print_data

    def prettify_data(self):
        """Prettifies all data, i.e. removes all newlines, tabs and spaces at
        end and beginning of data."""
        self.title_tag = file.prettify_str(self.title_tag)
        self.meta_description = file.prettify_str(self.meta_description)

        self.h1_headers = file.prettify_str_list(self.h1_headers)
        self.h2_headers = file.prettify_str_list(self.h2_headers)
        self.h3_headers = file.prettify_str_list(self.h3_headers)
        self.h4_headers = file.prettify_str_list(self.h4_headers)
        self.h5_headers = file.prettify_str_list(self.h5_headers)
        self.h6_headers = file.prettify_str_list(self.h6_headers)

    def add_comment(self, comment):
        """Adds a comment"""
        if self.comment:
            self.comment = self.comment + '\n' + comment
        else:
            self.comment = comment

    def _get_html_headers(self, soup, header_type):
        headers_list = soup.find_all(header_type)
        ret_headers = []
        for header in headers_list:
            if header.find('a'):
                comment = "%s headers contain Links" % header_type
                self.add_comment(comment)
            ret_headers.append(header.text)
        return ret_headers


def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())
