#!/usr/bin/python
# -*- coding: utf-8 -*-
import random, sys
from copy import deepcopy
from random import randint

def n(zahl):
	if zahl == None:
		return 0
	else:
		return zahl

def load_set(filename):
	f = open(filename, 'r')
	liste = f.readlines()
	for key, line in enumerate(liste):
		liste[key] = liste[key][1:-2]
		liste[key] = liste[key].split(", ")
	for key, line in enumerate(liste):
		for key2, color in enumerate(line):
			liste[key][key2].strip()
			liste[key][key2] = int(liste[key][key2].strip())
	return liste
	
def set_zeroes(whole_rectangle):
	for x_1 in xrange(0, 16):
		for x_2 in xrange(x_1+1, 17):
			for y_1 in xrange(0, 16):
				for y_2 in xrange(y_1+1,17):
					treffer = n(whole_rectangle[x_1][y_1])
					treffer+= n(whole_rectangle[x_2][y_1])
					treffer+= n(whole_rectangle[x_1][y_2])
					treffer+= n(whole_rectangle[x_2][y_2])
					if treffer > 3:
						print "Das Eingangsquadrat scheint fehlerhaft zu sein"
					if treffer == 3:
						if n(whole_rectangle[x_1][y_1]) == 0:
							whole_rectangle[x_1][y_1] = 0
						elif n(whole_rectangle[x_2][y_1]) == 0:
							whole_rectangle[x_2][y_1] = 0
						elif n(whole_rectangle[x_1][y_2]) == 0:
							whole_rectangle[x_1][y_2] = 0
						elif n(whole_rectangle[x_2][y_2]) == 0:
							whole_rectangle[x_2][y_2] = 0
		
def find_nones(whole_rectangle):
	none_list = []
	for x, row in enumerate(whole_rectangle):
		for y, position in enumerate(row):
			if position == None:
				none_list.append((x,y))
	return none_list

def count_ones(whole_rectangle):
	ones = 0
	for column in whole_rectangle:
		for color in column:
			if color == 1:
				ones += 1
	return ones
	
def check_new_zeroes(whole_rectangle, x, y):
	""" If I set a new 1 at (x,y), how many 0 do I have to set, which
		are not set jet? 
		Minimum: 0
		Maximum: (17-1)*2 ? """
	zero_list = []
	for x_tmp in xrange(0, 17):
		for y_tmp in xrange(0, 17):
			treffer = n(whole_rectangle[x_tmp][y_tmp]) + n(whole_rectangle[x][y_tmp]) + n(whole_rectangle[x_tmp][y])
			if treffer == 2:
				if whole_rectangle[x_tmp][y_tmp] == None:
					zero_list.append((x_tmp, y_tmp))
				elif whole_rectangle[x][y_tmp] == None:
					zero_list.append((x, y_tmp))
				elif whole_rectangle[x_tmp][y] == None:
					zero_list.append((x_tmp, y))
			elif treffer > 2:
				print "Oops ... something strange happened"
	return zero_list
	

def blub ():
	whole_rectangle = []
	whole_rectangle.append([1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,1,None,None,None,None,None,None,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,1,None,None,None,None,None,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,1,None,None,None,None,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,1,None,None,None,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,1,None,None,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,1,None,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,1,None,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,None,1,None,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,None,None,1,None,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,None,None,None,1,None,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,None,None,None,None,1,None,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,None,None,None,None,None,1,None,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,None,None,None,None,None,None,1,None,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,1,None])
	whole_rectangle.append([None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,1])
	

	liste = load_set('/home/moose/save-17-set1-74.txt')
	for x, row in enumerate(liste):
		for y, color in enumerate(row):
			if color == 1:
				whole_rectangle[x][y] = 0
	
	liste = load_set('/home/moose/save-17-set2-74.txt')
	for x, row in enumerate(liste):
		for y, color in enumerate(row):
			if color == 1:
				whole_rectangle[x][y] = 0
	liste = load_set('/home/moose/save-17-set3-69.txt')
	for x, row in enumerate(liste):
		for y, color in enumerate(row):
			if color == 1:
				whole_rectangle[x][y] = 0

	
	zaehlen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
	for x, row in enumerate(whole_rectangle):
		for y, color in enumerate(row):
			if color == 1:
				zaehlen[0][x] += 1 # Zählen der 1er in der x-ten Spalte
				zaehlen[1][y] += 1 # Zählen der 1er in der y-ten Zeile
		
		
	set_zeroes(whole_rectangle)
	
	nones = find_nones(whole_rectangle)

	while len(nones):
		min_nones = len(check_new_zeroes(whole_rectangle, nones[0][0], nones[0][1]))
		none_key = 0
		for none_key_tmp, none_pos in enumerate(nones):
			tmp_new_zeroes = len(check_new_zeroes(whole_rectangle, none_pos[0], none_pos[1]))
			if tmp_new_zeroes < min_nones and zaehlen[0][none_pos[0]] < 6 and zaehlen[1][none_pos[1]] < 6:
				min_nones = tmp_new_zeroes
				none_key = none_key_tmp
			if tmp_new_zeroes == min_nones and zaehlen[0][none_pos[0]] < 6 and zaehlen[1][none_pos[1]] < 6 and randint(0,1):
				min_nones = tmp_new_zeroes
				none_key = none_key_tmp
			#(zaehlen[0][none_pos[0]] <= 3 or zaehlen[1][none_pos[1]] <= 3)
		x, y = nones[none_key]
		new_zeroes = check_new_zeroes(whole_rectangle, x, y)
		for zero in new_zeroes:
			whole_rectangle[zero[0]][zero[1]] = 0
		whole_rectangle[x][y] = 1
		zaehlen[0][x] += 1
		zaehlen[1][y] += 1
		nones = find_nones(whole_rectangle)
	return whole_rectangle
	
i = 0
whole_rectangle = blub()
save_rect = []
save_rect_ones = count_ones(whole_rectangle)
print save_rect
print save_rect_ones
while save_rect_ones < 72 and i < 1000:
	whole_rectangle = blub()
	i += 1
	print i
	tmp_ones = count_ones(whole_rectangle)
	if tmp_ones > save_rect_ones:
		save_rect_ones = tmp_ones
		save_rect = whole_rectangle
		print str(save_rect_ones) + ": "
		for row in save_rect:	
			print row
print "i:" + str(i)
	
	
for row in save_rect:	
	print row
print "abc"
print save_rect
print "abc"
print count_ones(save_rect)
