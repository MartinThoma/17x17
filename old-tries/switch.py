#!/usr/bin/python
# -*- coding: utf-8 -*-

my_set = []





my_set.append([0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0])
my_set.append([1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0])
my_set.append([1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1])
my_set.append([0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0])
my_set.append([1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0])
my_set.append([0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1])
my_set.append([0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0])
my_set.append([0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0])
my_set.append([0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1])
my_set.append([1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0])
my_set.append([0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0])
my_set.append([0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,0])
my_set.append([1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0])
my_set.append([0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0])
my_set.append([0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0])
my_set.append([0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0])
my_set.append([0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1])

def nice_print(myset):
    print ":\t" + str([0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6])
    for line, data in enumerate(myset):
        print str(line) + ":\t" + str(data)

def check_set(myset):
    ones = 0
    for line,data in enumerate(myset):
        for pos, color in enumerate(data):
            if color == 1:
                ones += 1
                for i in xrange(pos+1,17):
                    if data[i] == 1:
                        for j in xrange(line+1, 17):
                            if myset[j][pos] == 1:
                                if myset[j][i] == 1:
                                    print "Found rectangle!:"
                                    print str((line,pos)) + str((line,i)) + str((j, pos)) + str((j, i))
                                    return False
    print "Found " + str(ones) + " ones in a " + str(len(myset)) + "x" + str(len(myset[0])) + " grid."
    return True

def switch_lines(myset, row1, row2):
    if row1 > row2:
        tmp = row1
        row1 = row2
        row2 = tmp
    row2_value = myset.pop(row2)
    row1_value = myset.pop(row1)

    myset.insert(row1, row2_value)
    myset.insert(row2, row1_value)

def switch_rows(myset, row1, row2):
    if row1 > row2:
        tmp = row1
        row1 = row2
        row2 = tmp
    for line, data in enumerate(myset):
        row1_tmp = data[row1]
        myset[line][row1] = data[row2]
        myset[line][row2] = row1_tmp
    

switch_lines(my_set, 12,0)
switch_lines(my_set, 9,3)
switch_lines(my_set, 3,0)
switch_lines(my_set, 15,5)
switch_lines(my_set, 10,7)
switch_lines(my_set, 4,1)
switch_lines(my_set, 13,9)
switch_lines(my_set, 12,10)
switch_lines(my_set, 4,0)
switch_lines(my_set, 9,10)
switch_lines(my_set, 16,13)
switch_lines(my_set, 11,13)
switch_lines(my_set, 15,16)

switch_rows(my_set, 12,15)
switch_rows(my_set, 8,14)
switch_rows(my_set, 6,13)
switch_rows(my_set, 5,12)
switch_rows(my_set, 7,9)
switch_rows(my_set, 12,15)


switch_rows(my_set, 0,16)
switch_rows(my_set, 2,15)
switch_rows(my_set, 3,13)
switch_rows(my_set, 5,12)
switch_rows(my_set, 10,11)

switch_lines(my_set, 2,11)
switch_lines(my_set, 6,14)
switch_lines(my_set, 7,12)

switch_lines(my_set, 7,6)
switch_lines(my_set, 8,7)
switch_lines(my_set, 9,8)
switch_lines(my_set,10,9)
switch_lines(my_set,10,0)
switch_lines(my_set,4,5)
switch_lines(my_set,4,1)
switch_lines(my_set,2,0)
switch_lines(my_set,2,4)
switch_lines(my_set,15,11)
switch_lines(my_set,14,12)
switch_lines(my_set,16,14)
switch_lines(my_set,15,16)

nice_print(my_set)
check_set(my_set)
