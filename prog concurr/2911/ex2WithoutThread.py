# -*- coding: utf-8 -*-
# Juin 2019
# Cours hippique
# Version très basique, sans mutex sur l'écran, sans arbitre, sans annoncer le gagant, ... ...
# Quelques codes d'échappement (tous ne sont pas utilisés)
import sys
import random
import math
import time
import os
import multiprocessing as mp
from multiprocessing import Process

len_array=20000000
Nb_process=20
mes_process=[]
vals_summed = mp.Array('i', Nb_process)
vals = []
start_time = ""


def main():
    sum_ = 0

    for i in range(0, len_array):
        vals.append(1)


    global start_time
    start_time = time.time()
    for i in range(0, len_array):
        sum_ += vals[i]

    print("sum : " + str(sum_))



if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    

