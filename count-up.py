#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from check_solution import *
from challenge17x17library import *
 
def fromDecToBase(number, base, digits):
    """ Convert a number of base "base" to base 10.
        This number will be padded from left with 0 until it has
        "digits" digits. """
    newNumber = ""
    while number > 0:
        rest = number % base
        newNumber = str(rest) + newNumber
        number -= rest
        number /= base
 
    return newNumber.zfill(digits)
 
def stringToRectange(baseColorString, m, n):
    rectangle = createEmpty(m,n)
    for x in xrange(0, m):
        for y in xrange(0,n):
            rectangle[x][y] = baseColorString[y*m+x]
    return rectangle
 
if __name__ == "__main__":
    from argparse import ArgumentParser
     
    parser = ArgumentParser()
    parser.add_argument("-m", "--width", dest="m", 
                        default=4, type=int, 
                        required=True, help="width")
    parser.add_argument("-n", "--height", dest="n", 
                        default=4, type=int, 
                        required=True, help="height")
    parser.add_argument("-colors", "--colors", dest="colors", 
                        default=2, type=int, 
                        required=True, help="height")
    parser.add_argument("-v", "--verbose",
                      action="store_true", dest="verbose",
                      default=False,
                      help="print solutions")
    args = parser.parse_args()
    m, n, colors = args.m, args.n, args.colors
     
    rectangle = createEmpty(m,n)
    nrOfCorrectSolutions = 0
    for coloring in xrange(1,colors**(m*n)):
        baseColorString = fromDecToBase(coloring, colors, m*n)
        rectangle = stringToRectange(baseColorString, m, n)
        errorList = getAllErrors(rectangle)
        if len(errorList) == 0:
            if args.verbose:
                print(rectangle)
            nrOfCorrectSolutions += 1
     
    print("There are %i correct solutions." % nrOfCorrectSolutions)
