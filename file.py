#!/usr/bin/env python3

import sys


def get_lines_from_file(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    pretty_lines = []

    for line in lines:
        pretty_lines.append(make_str_pretty(lines))

    return pretty_lines



def make_str_pretty(str_input):
    if str_input:
        str_pretty = str_input.replace('\n', ' ')
        str_pretty = str_pretty.replace('\r', ' ')
        str_pretty = str_pretty.replace('\t', ' ')
        str_pretty = str_pretty.strip()
    else:
        str_pretty = str_input

    return str_pretty


def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())
