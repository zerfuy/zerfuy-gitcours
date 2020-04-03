import math
import random
import time
from array import array
import random
import multiprocessing
import time
from multiprocessing import Array, Process, Pool

# Gabriel BAILLY
# Loic CAILLE

mes_process = []
N = 1000
Tab = Array('i', [random.randint(0, 2 * N) for _ in range(N)])

def merge(left, right):
    tableau = array('i', [])
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]: 
            tableau.append(left.pop(0))
        else: 
            tableau.append(right.pop(0))
    tableau += left + right
    return tableau

def merge_sort(Tableau, deb, fin):
    print("running from " + str(deb) + " to " + str(fin))
    Tableau[deb:fin] = sorted(Tableau[deb:fin])


def version_de_base(N):
    global Tab
    tabLen = len(Tab)    
    start = time.time()
    nbprocess = multiprocessing.cpu_count()

    for i in range(1, nbprocess + 1):  # Lancer nbProcessus
        deb = (tabLen//nbprocess) * i - tabLen//nbprocess
        fin = (tabLen//nbprocess) * i
        mes_process.append(Process(target=merge_sort, args=([Tab, deb, fin])))
        mes_process[i-1].start()

    for i in range(0, nbprocess):
        mes_process[i].join()

    a = array('i', [])
    b = array('i', [])

    a = merge(array('i', Tab[0:250]), array('i', Tab[250:500]))
    b = merge(array('i', Tab[500:750]), array('i', Tab[750:1000]))

    a = merge(a, b)
    print("taban : " + str(a))

    end = time.time()
    print("Le temps avec " + str(nbprocess) + " Process = %f pour un tableau de %d elems " 
        % ((end - start), N))

if __name__ == '__main__' :
    version_de_base(1000)


    # Le temps avec 6 Process = 0.019875 pour un tableau de 1000 elems
    # Le temps avec 4 Process = 0.015842 pour un tableau de 1000 elems
    # Le temps avec 2 Process = 0.009638 pour un tableau de 1000 elems
    # Le temps avec 1 Process = 0.007790 pour un tableau de 1000 elems


    # Le temps avec 6 Process = 0.406071 pour un tableau de 100000 elems
    # Le temps avec 1 Process = 0.273877 pour un tableau de 100000 elems

    # Le temps avec 6 Process = 34.843714 pour un tableau de 1000000 elems
    # Le temps avec 1 Process = 20.292294 pour un tableau de 1000000 elems