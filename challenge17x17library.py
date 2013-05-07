#!/usr/bin/python
# -*- coding: utf-8 -*-

def createEmpty(n, m):
    """ Create an empty rectangle which can be colored with four
        colors. """
    rectangle = []
    empty = []
    # Means: At this position, no square uses the color more often 
    # than 4-value times.
    for i in xrange(0, n):
        line = []
        for j in xrange(0, m):
            line.append({1:3, 2:3, 3:3, 4:3})
            empty.append((i,j))
        rectangle.append(line)
    return rectangle
