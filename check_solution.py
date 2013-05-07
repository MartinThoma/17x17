#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script checks if a solution is valid.
# It outputs the number of colors that were used and how big the
# rectangle was.
# Please note that the colored orbs should NOT be seperated by 
# spaces.

def getErrorList(rectangle, x1, y1):
    """ Check all rectangles for errors and return a list of all 
        errors, where (x1, y1) is the orb at the top left.
        Parameters:
          rectange
            a list of lists, filled with integers. Each integer is 
            one color.
          x1, y1
            two integers 
        Return: List with all errors found. 
                If none is found an empty list is returned. """
    m, n = len(rectangle), len(rectangle[0])
    errors = []
    left_top = rectangle[x1][y1]
 
    for x2 in xrange(x1+1, m):
        right_top = rectangle[x2][y1]
        for y2 in xrange(y1+1, n):
            left_bottom  = rectangle[x1][y2]
            right_bottom = rectangle[x2][y2]
            if left_top == left_bottom == right_top == right_bottom:
                errors.append([(x1,y1),(x1,y2),(x2, y1),(x2, y2)])
    return errors
 
def getAllErrors(rectangle):
    """ Parameter: rectangle, a list of list
        Returns  : A list of all errors found.
                   If none is found, an empty list is returned. """
    errors = []
    for x1, ebene in enumerate(rectangle):
        for y1, color in enumerate(ebene):
            errors_tmp = getErrorList(rectangle, x1, y1)
            for line in errors_tmp:
                errors.append(line)
    return errors
 
def getData(filename):
    """ Read the file.
        Returns: A list of strings (the lines). """
    data = []
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
      temp = line.strip()
      data.append(temp)
    return data
 
def getColors(myData):
    """ Returns: A list of all used colors """
    colors = []
    for line in myData:
        for color in line:
            if not color in colors:
                colors.append(color)
    return colors
 
if __name__ == "__main__":
    from argparse import ArgumentParser
     
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest="solutionfile", 
                    required=True,
                    help="Textfile with a solution",
                    metavar="FILE")
    parser.add_argument("-e", "--errors",
                    action="store_true", dest="display_errors", 
                    default=False,
           help="All errors of the solution file will be displayed.")
    args = parser.parse_args()

    rectangle = getData(args.solutionfile)
    color_list = getColors(rectangle)
    n = len(rectangle)
    m = len(rectangle[0])
    errors = getAllErrors(rectangle)
     
    print("%ix%i" % (n, m) )
    print("%i colors were used." % len(color_list) )
    print("%i errors are in the solution file." % len(errors) )
    if args.display_errors:
        for error in errors:
            print error
