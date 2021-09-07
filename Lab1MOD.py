import matplotlib
import numpy
import array

length = 1000
M = 2147483647
A = 16807
Q = 127773
R = 2836

def LemerRand(seed):
    hi = seed / Q
    lo = seed % Q
    seed = (A*lo) - (R * hi)
    if (seed<=0):
         seed = seed + M
    return seed / M

def matebal():
    someValue = array()
    i = 0
    while i < 15:
        someValue.insert(i,LemerRand(1000))
        i = i + 1
    print(numpy.var(someValue))