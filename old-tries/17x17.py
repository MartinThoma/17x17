#!/usr/bin/python
# -*- coding: utf-8 -*-
import random, sys
from copy import deepcopy

n = 17 # horizontal, position
m = 17 # vertikal, ebene

def create_empty(n, m):
    """ Erstellt ein leeres Viereck zum Färben mit max 4 Farben """
    rectangle = []
    empty = []
    #Means: At this position, no square uses the color more often than 4-value times.
    for i in xrange(0, n):
        line = []
        for j in xrange(0, m):
            line.append({1:3, 2:3, 3:3, 4:3})
            empty.append((i,j))
        rectangle.append(line)
    return rectangle

def get_color_of_orb(orb_dict):
    """ Uebergeben wird entweder ein int oder ein dict """
    orb_color = None
    if isinteger(orb_dict):
        return orb_dict
    for color, number in orb_dict.items():
        if number >= 1:
            if orb_color == None:
                orb_color = color
            else:
                return None
    return orb_color

def isinteger(x):
  try:
    return int(x) == x
  except:
    return False

def count_color_in_rectangle(color, orb1, orb2, orb3, orb4):
    count = 0
    if orb1 == color:
        count += 1
    if orb2 == color:
        count += 1
    if orb3 == color:
        count += 1
    if orb4 == color:
        count += 1
    return count

def new_orb_color_was_inserted(rectangle, ebene, position):
#   spaltencheck!!
    # alle vierecke in rectange durchgehen, von denen (ebene, position) ein teil ist
    global n
    global m

    orb_color = get_color_of_orb(rectangle[ebene][position])

    #neuer orb ist links oben:
    for i in xrange(ebene + 1, m):
        # rechts oben:
        links_unten = rectangle[i][position]
        for j in xrange(position + 1, n):
            rechts_oben = rectangle[ebene][j]
            rechts_unten = rectangle[i][j]
            
            new_min_for_orb_color = 3 - count_color_in_rectangle(orb_color, orb_color, links_unten, rechts_oben, rechts_unten)
            if not isinteger(links_unten):
                if(new_min_for_orb_color < rectangle[i][position][orb_color]):
                    rectangle[i][position][orb_color] = new_min_for_orb_color
            if not isinteger(rechts_oben):
                if(new_min_for_orb_color < rectangle[ebene][j]):
                    rectangle[ebene][j][orb_color] = new_min_for_orb_color
            if not isinteger(rechts_unten):
                if(new_min_for_orb_color < rectangle[i][j]):
                    rectangle[i][j][orb_color] = new_min_for_orb_color

    # neuer orb ist rechts oben:
    for i in xrange(ebene + 1, m):
        rechts_unten = rectangle[i][position]
        for j in xrange(0, position):
            links_oben = rectangle[ebene][j]
            links_unten = rectangle[i][j]

            new_min_for_orb_color = 3 - count_color_in_rectangle(orb_color, orb_color, links_unten, links_oben, rechts_unten)
            if not isinteger(rechts_unten):
                if(new_min_for_orb_color < rectangle[i][position][orb_color]):
                    rectangle[i][position][orb_color] = new_min_for_orb_color
            if not isinteger(links_oben):
                if(new_min_for_orb_color < rectangle[ebene][j]):
                    rectangle[ebene][j][orb_color] = new_min_for_orb_color
            if not isinteger(links_unten):
                if(new_min_for_orb_color < rectangle[i][j]):
                    rectangle[i][j][orb_color] = new_min_for_orb_color

    # neuer orb ist links unten:
    for i in xrange (0, ebene):
        links_oben = rectangle[i][position]
        for j in xrange(position + 1, n):
            rechts_oben = rectangle[i][j]
            rechts_unten= rectangle[ebene][j]

            new_min_for_orb_color = 3 - count_color_in_rectangle(orb_color, orb_color, links_oben, rechts_oben, rechts_unten)
            if not isinteger(links_oben):
                if(new_min_for_orb_color < rectangle[i][position][orb_color]):
                    rectangle[i][position][orb_color] = new_min_for_orb_color
            if not isinteger(rechts_oben):
                if(new_min_for_orb_color < rectangle[i][j]):
                    rectangle[i][j][orb_color] = new_min_for_orb_color
            if not isinteger(rechts_unten):
                if(new_min_for_orb_color < rectangle[ebene][j]):
                    rectangle[ebene][j][orb_color] = new_min_for_orb_color


    #neuer orb ist rechts unten:
    for i in xrange(0, ebene):
        rechts_oben = rectangle[i][position]
        for j in xrange(0, position):
            links_oben = rectangle[i][j]
            links_unten= rectangle[ebene][j]

            new_min_for_orb_color = 3 - count_color_in_rectangle(orb_color, orb_color, links_oben, rechts_oben, links_unten)
            if not isinteger(rechts_oben):
                if(new_min_for_orb_color < rectangle[i][position][orb_color]):
                    rectangle[i][position][orb_color] = new_min_for_orb_color
            if not isinteger(links_oben):
                if(new_min_for_orb_color < rectangle[i][j]):
                    rectangle[i][j][orb_color] = new_min_for_orb_color
            if not isinteger(links_unten):
                if(new_min_for_orb_color < rectangle[ebene][j]):
                    rectangle[ebene][j][orb_color] = new_min_for_orb_color

def print_dict_nice(rect):
    global n
    global m
    print "Das Quadrat:"
    for ebene in  xrange(0,m):
        for pos in xrange(0,n):
            tmp = get_color_of_orb(rect[ebene][pos])
            if tmp == None:
                sys.stdout.write(str(rect[ebene][pos]) + "\t")
            else:
                sys.stdout.write(str(tmp) + "\t\t\t\t\t\t")
        sys.stdout.write("\n")


def random_color(dictionary):
    liste = []
    pref_color = None
    pref_count = 0
    for color, number in dictionary.items():
        if number > 0:
            liste.append(color)
            if number > pref_count:
                pref_color = color
                pref_count = number
    #return random.choice(liste)
    if pref_color == None:
        sys.exit("Error, no possibilities at this point")
    return pref_color

def find_next_empty(rect):
    global maxsquare
    j = True
    while j:
        max_x = maxsquare
        max_y = maxsquare
        for y in range(max_y, -1, -1):
          if y == max_y:
            for x in xrange(0, max_x + 1):
                if not isinteger(rect[y][x]):
                    return (y, x)
          else:
            if not isinteger(rect[y][max_x]):
                return (y, max_x)
            if y == 0:
                max_x += 1
                max_y+=1
        maxsquare += 1

def change_random_pos(rect):
    global m
    global n

    ebene, position = find_next_empty(rect)
    insert_new_orb(rect, ebene, position, random_color(rect[ebene][position]))
    return (ebene, position)

def save_to_file(rect):
    f = open("/home/moose/17x17/solution.txt", 'w')
    for line in rect:
        tmp = " ".join(["%s" % el for el in line]) + "\n"
        f.write(tmp)
    f.close()

def is_only_one_rest(orbs_dict):
    possible_colors = []
    for color, number in orbs_dict.items():
        if number > 0:
            possible_colors.append(color)
    if len(possible_colors) == 1:
        return possible_colors[0]
    else:
        return False

def check_for_deps(rect):
    global m
    global n

    for ebene in xrange(0, m):
        for position in xrange(0,n):
            if not isinteger(rect[ebene][position]):
                color = is_only_one_rest(rect[ebene][position])
                if color:
                    insert_new_orb(rect, ebene, position, color)
                    return True
    return False

def insert_new_orb(rect, ebene, position, color):
    global not_solved
    not_solved -= 1
    rect[ebene][position] = color
    new_orb_color_was_inserted(rect, ebene, position)

rect = create_empty(n,m)
not_solved = n*m
insert_new_orb(rect, 0, 0, 1)
insert_new_orb(rect, 0, 1, 2)
insert_new_orb(rect, 1, 0, 1)

i = 0
maxsquare = 0

while not_solved:
    ebene, position = change_random_pos(rect)
    while check_for_deps(rect):
        pass


save_to_file(rect)
