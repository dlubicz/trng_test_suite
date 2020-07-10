#!/usr/bin/python
import sys
import math
from math import *

from source_mod_time import *

alpha=[0.5]
memory = 1

f = TimeFunction(0,1,5000, 1)
f.TFdirac(0.25)

ratio_slope = [3]


facteur = 10**-6
ratio_pente = [facteur * i for i in ratio_slope]
kd= 13600
ratio_pente_kd = [kd * i for i in ratio_pente]

print trng_entropy(alpha, f, memory, 14, ratio_pente_kd, True) 
print find_waiting_time(alpha, f, memory, 14, ratio_pente, [5000,10000], 0.997, 0.001, True)
