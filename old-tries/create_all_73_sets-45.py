#!/usr/bin/python
# -*- coding: utf-8 -*-
from copy import deepcopy

def create_empty(n, m):
    """ Erstellt ein leeres Viereck zum Färben mit max 4 Farben """
    rectangle = []
    empty = []
    #Means: At this position, no square uses the color more often than 4-value times.
    for i in xrange(0, n):
        line = []
        for j in xrange(0, m):
            line.append(None)
            empty.append((i,j))
        rectangle.append(line)
    return rectangle

def check_all_left_top(rectangle, x1, y1):
    # check for errors:
    # die aktuelle kugel (x1, y1) ist links oben
    error_list = []
    links_oben = rectangle[x1][y1]

    for x2 in xrange(x1+1, 17):
        rechts_oben = rectangle[x2][y1]
        for y2 in xrange(y1+1, 17):
            links_unten  = rectangle[x1][y2]
            rechts_unten = rectangle[x2][y2]
            if links_oben == links_unten == rechts_oben == rechts_unten:
                return False
    return True

def get_all_errors(rectangle):
    errors = []
    for x1, ebene in enumerate(rectangle):
        for y1, farbe in enumerate(ebene):
            errors_tmp = check_all_left_top(rectangle, x1, y1)
            for line in errors_tmp:
                errors.append(line)
    return errors

def get_my_73_set(rectangle, setsize):
    for x1 in xrange(0,17):
        for y1 in xrange(0,17):
            if rectangle[16-x1][16-y1] == None:
                for color in [1,0]:
                    rectangle_tmp = deepcopy(rectangle)
                    rectangle_tmp[16-x1][16-y1] = color
                    
                    if color == 1:
                        if not check_all_left_top(rectangle_tmp, 16-x1, 16-y1):
                            continue
                        else:
                            setsize_tmp = setsize + 1
                            if setsize_tmp >= 73:
                                return rectangle_tmp
                            else:
                                solution_tmp = get_my_73_set(rectangle_tmp, setsize_tmp)
                                if solution_tmp != False:
                                    return solution_tmp
                    else:
                        solution_tmp = get_my_73_set(rectangle_tmp, setsize)
                        if solution_tmp != False:
                            return solution_tmp

    return False

print get_my_73_set(create_empty(17, 17), 0)

