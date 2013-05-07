#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from math import ceil

def newRect(m=4, n=4):
    """ Initialisiere Datenstruktur 
        Zeile zuerst, Spalte später
    """
    rectangle = [[0 for i in xrange(0, n)] for j in xrange(0, m)]
    return rectangle

def printRect(rect):
    for line in rect:
        print line

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
    #print("Zeile: %i" % zeile)
    #print("Spalte: %i" % spalte)
    kugel4 = rect[zeile][spalte]
    n = len(rect[0])
    for zeile2 in xrange(zeile-1,-1,-1):
        kugel2 = rect[zeile2][spalte]
        for spalte2 in xrange(spalte-1,-1,-1):
            #print("Check_error:")
            #print("(%i|%i)\t(%i|%i)" % (zeile2, spalte2, zeile2, spalte))
            #print("(%i|%i)\t(%i|%i)" % (zeile, spalte2, zeile, spalte))
            kugel1 = rect[zeile2][spalte2]
            kugel3 = rect[zeile][spalte2]

            if kugel1 == kugel2 == kugel3 == kugel4:
                return [(zeile, spalte), (zeile, spalte2), (zeile2, spalte), (zeile2, spalte2)]
    return False

def correct_error(rect, error, colors, n, steps):
    """ error muss eine liste aus vier tupeln sein. Die tupel sind nach
        (zeile, spalte) aufgebaut. Der erste Tupel ist der unwichtigste, der
        letzte der wichtigste.
    """

    if rect[error[0][0]][error[0][1]] +1 == colors:
        zeile = error[0][0]
        spalte = error[0][1]
        while rect[zeile][spalte] + 1 == colors:
            rect[zeile][spalte] = 0
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
        return False
    else:
        rect[error[0][0]][error[0][1]] += 1

def nr_of_steps_in_bf(rect, colors, m, n):
    steps = 0
    stelle = 0
    for zeile in xrange(m-1,-1,-1):
        for spalte in xrange(n-1,-1,-1):
            steps += rect[zeile][spalte]*colors**stelle
            stelle += 1
    return steps

def getCorrectRectangle(rect, m, n, colors, steps):
    correctedError = False

    i = 0

    while True and i < 100000000:
        i += 1
        if i % 100000 == 0:
            print("##########################################i: %i" % i)
            printRect(rect)
        for zeile in xrange(0, m):
            for spalte in xrange(0, n):
                #print("Zeile / Spalte: (%i|%i)" % (zeile, spalte))
                error = check_error(rect, zeile, spalte)
                if error != False:
                    correct_error(rect, error, colors, n, steps + i)
                    #print("###### (corrected error)")
                    #printRect(rect)
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

def getCorrectMiniRect(rect, square, colors, steps):
    miniRect = newRect(square, square)
    for i in xrange(0, square):
        for j in xrange(0, square):
            #print("(%i|%i)" % (i, j))
            miniRect[i][j] = rect[i][j]
    steps = getCorrectRectangle(miniRect, square, square, colors, steps)
    printRect(miniRect)
    return (steps, miniRect)

def kacheln(rect, minirect, m, n):
    i = len(minirect)
    j = len(minirect[0])

    for zeile in xrange(0, m):
        for spalte in xrange(0, n):
            rect[zeile][spalte] = minirect[zeile%i][spalte%j]

def main():
    m = 14
    n = 14
    colors = 4
    rect = newRect(m, n)

    #initialise
    if True:
        blocklength = int(ceil(float(n) / colors))
        for zeile in xrange(0, m):
            counter = 0
            c = 0
            for spalte in xrange(0, n):
                rect[zeile][spalte] = c
                counter += 1
                if counter == blocklength:
                    counter = 0
                    c += 1

    miniRect = [[0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 2, 2, 2, 2],
    [0, 1, 2, 3, 3, 3],
    [0, 2, 3, 1, 2, 3],
    [0, 2, 3, 1, 3, 2]]
    kacheln(rect, miniRect, m, n)

    square = 7
    steps_good = 0

    while square < min(m,n):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Steps so far: %i" % steps_good)
        printRect(rect)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("minirect: %i" % square)
        steps, miniRect = getCorrectMiniRect(rect, square, colors, steps_good)
        steps_good += steps
        print("minirect")
        kacheln(rect, miniRect, m, n)
        printRect(rect)
        square += 1
        print("Square-Size: %i" % square)
    sys.exit()
    print("continue the normal way...")

    steps_good = getCorrectRectangle(rect, m, n, colors, steps_good)
    printRect(rect)
    steps_bf = nr_of_steps_in_bf(rect, colors, m, n)
    print("Brute-Force would have needed %i steps." % steps_bf)
    print("So this algorithm needed only %f %% of BF." % ((float(steps_good) / steps_bf)*100))

if __name__ == "__main__":
    main()
