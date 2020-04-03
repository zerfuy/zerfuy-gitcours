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




def proc_sem(i):

    range_calc = int(len_array/Nb_process)
    offset = i * range_calc
    sum_ = 0

    for j in range(0, range_calc):
        sum_ += vals[offset + j]

    vals_summed[i] = sum_
    

def main():
    mes_sem = []

    for i in range(0, len_array):
        vals.append(1)

    sum_ = 0
    i = 0

    global start_time
    start_time = time.time()
    for i in range(0, Nb_process):  # Lancer Nb_process processus
        mes_process.append(Process(target=proc_sem, args=(i, )))
        mes_process[i].start()

    for i in range(Nb_process):
        mes_process[i].join()
        print("finished")

    for i in range(Nb_process):
        sum_ += vals_summed[i]

    print("sum : " + str(sum_))



if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    

