#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup


class WebPage(object):
    def __init__(self, url, soup):
        self.url = url
        if not isinstance(soup, BeautifulSoup):
            raise TypeError("bar must be set to an integer")
        self.soup = soup

    def get_numbers_of_headers(self):
        """Returns a 6 fold tuple with the numbers of h1 - 6h headers"""
        return (len(self.h1_headers), len(self.h2_headers),
                len(self.h3_headers), len(self.h4_headers),
                len(self.h5_headers), len(self.h6_headers))

    def get_meta_description(self):
        """Returns webpage's meta description"""
        soup_meta_desc = self.soup.findAll('meta',
                                           attrs={"name": "description"})
        descr_content = soup_meta_desc[0]['content']
        return descr_content

    def get_title_tag(self):
        """Returns web page's title tag"""
        return self.soup.title.string

    def get_h1_headers(self):
        """Returns all h1 html headers"""
        return self.soup.find_all('h1')

    def get_h2_headers(self):
        """Returns all h2 html headers"""
        return self.soup.find_all('h2')

    def get_h3_headers(self):
        """Returns all h3 html headers"""
        return self.soup.find_all('h3')

    def get_h4_headers(self):
        """Returns all h4 html headers"""
        return self.soup.find_all('h4')

    def get_h5_headers(self):
        """Returns all h5 html headers"""
        return self.soup.find_all('h5')

    def get_h6_headers(self):
        """Returns all h6 html headers"""
        return self.soup.find_all('h6')


def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())
