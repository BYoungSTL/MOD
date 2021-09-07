import numpy
import array


def main():
    length = 1000
    M = 2147483647
    A = 16807
    Q = 127773
    R = 2836
    seed = 4545

    someValue = []
    i = 0
    while i < 1000:
        hi = seed / Q
        lo = seed % Q
        seed = (A*lo) - (R * hi)
        if (seed<=0):
            seed = seed + M     
        seed = seed / M
        someValue.insert(i, seed)
        i = i + 1
    print(someValue)
    print(numpy.var(someValue, axis=0))

main()