#!/usr/bin/env python3

import sys


def get_lines_from_file(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    pretty_lines = []

    for line in lines:
        pretty_lines.append(prettify_str(line))

    return pretty_lines


def prettify_str(str_input):
    if str_input:
        str_pretty = str_input.replace('\n', ' ')
        str_pretty = str_pretty.replace('\r', ' ')
        str_pretty = str_pretty.replace('\t', ' ')
        str_pretty = str_pretty.strip()
    else:
        str_pretty = str_input

    return str_pretty


def prettify_str_list(list_input):
    pretty_list = []
    for str_input in list_input:
        pretty_list.append(prettify_str(str_input))

    return pretty_list


def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())
