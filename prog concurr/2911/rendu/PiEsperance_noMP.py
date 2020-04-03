# -*- coding: utf-8 -*-
# Gabriel BAILLY
# Loic CAILLE

import math, random, time, numpy
from array import array
     
if __name__ == "__main__":
    N = 1000
    somme = 0
    tab = numpy.linspace(0,1,N)
    for j in range (N):
        somme += math.sqrt(1-(tab[j]*tab[j]))
    
    QUART_PI = somme / N
    PI = QUART_PI * 4
    
    print("PI : {}".format(PI))