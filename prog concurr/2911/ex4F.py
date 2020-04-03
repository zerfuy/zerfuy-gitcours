
# -*- coding: utf-8 -*-

import math
import random
from array import array
import time
import multiprocessing
from multiprocessing import Pool, Process, Value
from threading import Thread
import threading
import _thread


mes_process=[]
Nb_Process = 4
a = Value('i', 0)

#Ce programme a été fait avec des threads pour changer des process

def qsort(tabset, left, right):
    print("thread {0} is sorting {1}".format(threading.current_thread(), tabset[left:right]))

    i = left
    j = right
    pivot = tabset[int((left + right)/2)]
    tmp = 0
    while(i <= j):
         while(pivot > tabset[i]):
             i = i+1
         while(pivot < tabset[j]):
             j = j-1
         if(i <= j):
             tmp = tabset[i]     
             tabset[i] = tabset[j]
             tabset[j] = tmp
             i = i + 1
             j = j - 1

    lthread = None
    rthread = None

    if (left < j):
        lthread = Thread(target = lambda: qsort(tabset,left,j))
        lthread.start()

    if (i < right):
        rthread = Thread(target=lambda: qsort(tabset,i,right))
        rthread.start()

    if lthread is not None: lthread.join()
    if rthread is not None: rthread.join()
    return tabset

def version_de_base(N):
    Tab = array('i', [random.randint(0, 2 * N) for _ in range(N)])
    tabLen = len(Tab)    
    print("tab len : ", tabLen)

    start = time.time()

    qsort(Tab, 0, len(Tab) - 1)

    end = time.time()
    print("Apres : ", Tab)
    print("Le temps avec une multitude de threads = %f pour un tableau de %d elems " 
        % ((end - start) * 1000, N))

if __name__ == '__main__':
    version_de_base(1000)