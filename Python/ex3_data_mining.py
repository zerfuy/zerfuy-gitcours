# -*- coding: utf-8 -*-

import numpy as np
dataset = np.loadtxt("pl.csv", dtype={'names': ('name', 'year'), 'formats': ('U100', 'i4')}, skiprows=1, delimiter=",", encoding="UTF-8")
print(dataset)