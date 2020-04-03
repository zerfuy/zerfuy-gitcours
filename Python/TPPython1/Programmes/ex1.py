#!/usr/bin/python3
# coding: utf-8


def main():
    n = input("saisir un entier wola : \n")
    n = int(n)

    for i in range(1, n+1):
        s = ""
        for j in range(1, i+1):
            s += str(j)
        print(s)

if __name__ == '__main__':
    main()