
# -*- coding: utf-8 -*-

import math
import random
from array import array
import time
import multiprocessing
from multiprocessing import Pool, Process, Value
from threading import Thread
import threading
import thread
import math


mes_process=[]


def run(min, max):
    print("min : " + str(min) + "max : " + str(max))
    for i in range(min, max, 2):
        prime = True
        for j in range(min, int(math.sqrt(i))+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(str(i) + " est premier")

if __name__ == '__main__': 
    start = time.time()

    max = 1000
    nbproc = 8

    for i in range(1, nbproc + 1):
        arg = max//i
        mes_process.append(Process(target=run, args=(arg - (max // nbproc) + 1, arg, )))
        mes_process[i-1].start()

    for i in range(1, nbproc + 1):
        mes_process[i-1].join()