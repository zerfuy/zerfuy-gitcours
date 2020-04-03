#!/usr/bin/python3
# coding: utf-8

import argparse
import os
from collections import Counter


def main():
    parser = argparse.ArgumentParser(description='directory Name.')
    parser.add_argument('dirName', type=str, help='a directory Name.')
    args = parser.parse_args()

    print("currentpath", "folders", "files")
    for currentpath, folders, files in os.walk(args.dirName):
        print(currentpath, folders, files)


if __name__ == '__main__':
    main()