#!/usr/bin/python
import sys
import math
from math import *

from source_mod_time import *

alpha=[0.5]
memory = 1
min = float(0)
max = float(0.1)
nb_points = 10
nb_xor = 1

f = TimeFunction(0,1,5000, 1)
f.TFdirac(0.25)


output = open('temp/qgraph.txt', 'w')
for i in range(1,nb_points):
    quality_factor = min + (max-min)/nb_points*i
    quality_factor_list = [quality_factor]*nb_xor
    print quality_factor,  trng_entropy(alpha, f, memory, nb_xor, quality_factor_list, False)
    output.write(str(quality_factor))
    output.write(" ")
    output.write(str(trng_entropy(alpha, f, memory, nb_xor, quality_factor_list, False)))
    output.write("\n")
output.close()
