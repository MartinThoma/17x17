#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser
from math import ceil
from copy import deepcopy
 
def newRect(m=4, n=4):
    """ Initialisiere Datenstruktur 
        Zeile zuerst, Spalte später
    """
    rectangle = [[0 for i in xrange(0, n)] for j in xrange(0, m)]
    return rectangle
 
def printRect(rect):
    #print("##%s" % [i for i in xrange(0, len(rect))])
    for i, line in enumerate(rect):
        print("%i\t%s" % (i, line))
    print(" ")
 
def check_all_left_top(rectangle, x1, y1):
    # Auf Fehler überprüfen:
    # Die aktuelle kugel (x1, y1) ist links oben
    error_list = []
    links_oben = rectangle[x1][y1]
 
    for x2 in xrange(x1+1, m):
        rechts_oben = rectangle[x2][y1]
        for y2 in xrange(y1+1, n):
            links_unten  = rectangle[x1][y2]
            rechts_unten = rectangle[x2][y2]
            if links_oben == links_unten == rechts_oben == rechts_unten:
                error_list.append([(x1,y1),(x1,y2), (x2, y1), (x2, y2)])
    return error_list
 
def get_all_errors(rectangle):
    errors = []
    for x1, ebene in enumerate(rectangle):
        for y1, farbe in enumerate(ebene):
            errors_tmp = check_all_left_top(rectangle, x1, y1)
            for line in errors_tmp:
                errors.append(line)
    return errors
 
def check_error(rect, zeile, spalte):
    """ Überprüft, ob an der Stelle (zeile, spalte) ein Fehler ist.
        Dabei gehe ich davon aus, dass bereits alle weniger wichtigen Kugeln 
        bereits überprüft wurden. Falls ein Fehler vorhanden ist, wird eine 
        Liste aus vier Tupeln zurückgegeben. 
        (0,0) ist am wichtigsten. 
 
        (zeile2,    spalte2)    (zeile2, spalte)
        (zeile,     spalte2)    (zeile,  spalte)
    """
    kugel4 = rect[zeile][spalte]
    for zeile2 in xrange(zeile-1,-1,-1):
        kugel2 = rect[zeile2][spalte]
        for spalte2 in xrange(spalte-1,-1,-1):
            kugel1 = rect[zeile2][spalte2]
            kugel3 = rect[zeile][spalte2]
 
            if kugel1 == kugel2 == kugel3 == kugel4:
                return [(zeile, spalte), (zeile, spalte2), (zeile2, spalte), (zeile2, spalte2)]
    return False
 
def correct_error(rect, error, steps, colors, n):
    """ error muss eine liste aus vier tupeln sein. Die tupel sind nach
        (zeile, spalte) aufgebaut. Der erste Tupel ist der unwichtigste, der
        letzte der wichtigste.
    """

    changedRows = []
 
    if rect[error[0][0]][error[0][1]] +1 == colors:
        zeile = error[0][0]
        spalte = error[0][1]
        while rect[zeile][spalte] + 1 == colors:
            rect[zeile][spalte] = 0
            changedRows.append(zeile)
            spalte -= 1
            if spalte == -1:
                spalte += n
                zeile -= 1
            if spalte == -1 or zeile == -1:
                print("No solution possible.")
                print("##########################################i: %i" % steps)
                printRect(rect)
                sys.exit()
 
        rect[zeile][spalte] += 1
        return changedRows
    else:
        rect[error[0][0]][error[0][1]] += 1
        changedRows.append(error[0][0])
        return changedRows
 
def nr_of_steps_in_bf(rect, m, n, colors):
    steps = 0
    stelle = 0
    for zeile in xrange(m-1,-1,-1):
        for spalte in xrange(n-1,-1,-1):
            steps += rect[zeile][spalte]*colors**stelle
            stelle += 1
    return steps

def getColorDiff(row):
    min_color = len(row)
    max_color = 0
    for el in row:
        counter = row.count(el)
        if counter < min_color:
            min_color = counter
        if counter > max_color:
            max_color = counter
    return (min_color, max_color)

def add(rect, zeile, spalte, colors):
    rect[zeile][spalte] += 1
    while rect[zeile][spalte] == colors:
        rect[zeile][spalte] = 0
        spalte -= 1
        if spalte == -1:
            spalte = len(rect[0])-1
            zeile -= 1
            if zeile == -1:
                return False
        rect[zeile][spalte] += 1
    return True

def addRow(rect, zeile, spalte, colors):
    rect[zeile][spalte] += 1
    returnVal = True
    while rect[zeile][spalte] == colors:
        rect[zeile][spalte] = 0
        zeile -= 1
        if zeile == -1:
            zeile = len(rect) - 1
            spalte -= 1
            returnVal = 1
            if spalte == -1:
                return False
        rect[zeile][spalte] += 1
    return returnVal

def normalize_rows(rect, colors):
    #print("<normalize_rows>")
    changesDone = False
    for row in xrange(0, len(rect)):
        min_color, max_color = getColorDiff(rect[row])
        while abs(max_color - min_color) > 1 or len(set(rect[row])) < colors:
            add(rect, row, len(rect[0])-1, colors)
            changesDone = True
            min_color, max_color = getColorDiff(rect[row])
    #print("</normalize_rows>")
    return changesDone

def getSpalte(rect, spaltenNr):
    spalte = []
    for zeile in xrange(0, len(rect)):
        spalte.append(rect[zeile][spaltenNr])
    return spalte

def normalize_columns(rect, colors):
    #print("<normalize_columns>")
    changesDone = False
    for spaltenNr in xrange(0, len(rect[0])):
        spalte = getSpalte(rect, spaltenNr)
        min_color, max_color = getColorDiff(spalte)
        while abs(max_color - min_color) > 1 or len(set(spalte)) < colors:
            ret = addRow(rect, len(rect)-1, spaltenNr, colors)
            if ret == False:
                printRect(rect)
                sys.exit("readyhow.")
            elif ret == 1:
                return True
            changesDone = True
            spalte = getSpalte(rect, spaltenNr)
            min_color, max_color = getColorDiff(spalte)
            #print("min: %i, max: %i, colors: %i von %i" % (min_color, max_color, len(set(spalte)), colors))
    #print("</normalize_columns>")
    return changesDone

def getCorrectRectangle(rect, m, n, colors, granularity):
    normalize_rows(rect, colors)

    correctedError = False
 
    i = 0
 
    while True and i < 1000000:
        i += 1
        if i % granularity == 0:
            print("#############################################################i: %i" % i)
            printRect(rect)
        for zeile in xrange(0, m):
            for spalte in xrange(0, n):
                error = check_error(rect, zeile, spalte)
                if error != False:
                    changedRows = correct_error(rect, error, i, colors, n)
                    correctedError = True
                    j = 0
                    c2 = False
                    while correctedError or c2:
                        #correctedError = normalize_columns(rect, colors)
                        correctedError = normalize_rows(rect, colors)
                    #printRect(rect)
                    #print("")
                    correctedError = True

                    break
                """
                if weitermachen == False:
                    print("Abort. (%i|%i)" % (zeile, spalte))
                    return False"""
            if correctedError:
                break
        if correctedError:
            correctedError = False
        else:
            print("Found solution after %i steps" % i)
            return i
    return i

def getRandomPermutation(n, colors):
    mySet = [i % colors for i in xrange(0, int(ceil(float(n)/colors)*colors))]
    sortedSet = sorted(mySet)
    
    yield mySet

def main():
    parser = OptionParser()
    parser.add_option("-m", type="int", default=4, dest="m", help="Zeilen")
    parser.add_option("-n", type="int", default=4, dest="n", help="Spalten")
    parser.add_option("-c", type="int", default=2, dest="colors", help="Farben")
    parser.add_option("-g", type="int", default=10000, dest="granularity", 
                    help="Wie feingranular soll das Ergebnis ausgegeben werden?")
    (options, args) = parser.parse_args()
    m = options.m
    n = options.n
    colors = options.colors
 
    rect = newRect(m, n)

    steps_good = getCorrectRectangle(rect, m, n, colors, options.granularity)
    printRect(rect)
    steps_bf = nr_of_steps_in_bf(rect, m, n, colors)
    print("Brute-Force would have needed %i steps." % steps_bf)
    print("So this algorithm needed only %f %% of BF." % ((float(steps_good) / steps_bf)*100))

if __name__ == "__main__":
    main()
