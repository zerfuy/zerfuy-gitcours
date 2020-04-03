#!/usr/bin/python3
# coding: utf-8

import argparse
from collections import Counter


def main():
    parser = argparse.ArgumentParser(description='Process filename.')
    parser.add_argument('fileName', type=str, help='a fileName')
    args = parser.parse_args()

    nbChars = 0
    nbLines = 0
    nbWords = 0
    nbUniqueWords = 0
    words = []

    with open(args.fileName, "r") as file:
        words = file.read().split()
        nbWords += len(words)
        nbUniqueWords = len(set(words))
        file.seek(0)
        for line in file:
            nbLines += 1
            for ch in line:
                nbChars += 1


    print("nbChars : " + str(nbChars))
    print("nbLines : " + str(nbLines))
    print("nbWords : " + str(nbWords))
    print("nbUniqueWords : " + str(nbUniqueWords))
    print("20 first words (or less, if there are less than 20 words) : ")
    n = 0
    while n < nbWords and n < 20:
        print(words[n])
        n += 1

if __name__ == '__main__':
    main()