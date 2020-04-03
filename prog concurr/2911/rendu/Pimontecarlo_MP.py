
import random
import multiprocessing
import time
from multiprocessing import Pool

# Gabriel BAILLY
# Loic CAILLE

def monte_carlo_pi_part(n):

    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()

        # Inside
        if x*x + y*y <= 1:
            count = count+1

    return count


if __name__ == '__main__':

    start = time.time()
    np = multiprocessing.cpu_count()
    print(('You have {0:1d} CPUs'.format(np)))
    n = 10000000

    part_count = [n//np for i in range(np)]
    pool = Pool(processes=np)
    count = pool.map(monte_carlo_pi_part, part_count)

    end = time.time()
    print("Le temps avec " + str(np) + " Process = %f " 
        % ((end - start)))

    print(("Pi:: ", sum(count)/(n*1.0)*4))


    # You have 6 CPUs
    # Le temps avec 6 Process = 0.456627
    # ('Pi:: ', 3.1414544)

    # You have 4 CPUs
    # Le temps avec 4 Process = 0.488921
    # ('Pi:: ', 3.1425252)

    # You have 2 CPUs
    # Le temps avec 2 Process = 0.899756
    # ('Pi:: ', 3.1409568)

    # You have 1 CPUs
    # Le temps avec 1 Process = 1.789997
    # ('Pi:: ', 3.141706)