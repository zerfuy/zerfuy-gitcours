
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
import math
from decimal import Decimal, getcontext


# Python calculus with BBP method

if __name__ == '__main__': 
    
    getcontext().prec=100
    print(sum(1/Decimal(16)**k * 
          (Decimal(4)/(8*k+1) - 
           Decimal(2)/(8*k+4) - 
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(100)))