# -*- coding: utf-8 -*-
# Gabriel BAILLY
# Loic CAILLE

import math
import random
import time
import os
from statistics import mean
import multiprocessing as mp
from multiprocessing import Process

np = mp.cpu_count()
vals = mp.Array('f', np)
mes_process = []

def run(vals, index, min, max):
    somme = 0
    for i in range(1, max):
        div = 1 + (((i-0.5)/max)*((i-0.5)/max))
        somme += (4/div)
    somme = 1/max * somme
    vals[index] = somme

if __name__ == '__main__':
    start = time.time()
    np = mp.cpu_count()
    print(('You have {0:1d} CPUs'.format(np)))

    max = 100000

    for i in range(1, np+1):
        mes_process.append(Process(target=run, args=(vals, i-1, (max/np*i)-max/np, int(max/np*i))))
        mes_process[i-1].start()

    for i in range(np):
        mes_process[i].join()
        print("finished")

    end = time.time()
    print("Time with " + str(np) + " Process = %f " % ((end - start)))
    print(str(np) + " estimations : ")
    for i  in range(0, np):
        print(str(vals[i]))
    print(("Pi:: ", str(mean(vals))))

    # Time with 6 Process = 0.034836
    # Time with 4 Process = 0.030232
    # Time with 2 Process = 0.025927
    # Time with 1 Process = 0.022815