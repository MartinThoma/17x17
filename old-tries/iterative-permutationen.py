#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import deepcopy
import random

def next_permutation(seq, pred=cmp):
    """Like C++ std::next_permutation() but implemented as
    generator. Yields copies of seq."""
    def reverse(seq, start, end):
        # seq = seq[:start] + reversed(seq[start:end]) + \
        #       seq[end:]
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1
    if not seq:
        raise StopIteration
    try:
        seq[0]
    except TypeError:
        raise TypeError("seq must allow random access.")
    first = 0
    last = len(seq)
    seq = seq[:]
    # Yield input sequence as the STL version is often
    # used inside do {} while.
    yield seq
    if last == 1:
        raise StopIteration
    while True:
        next = last - 1
        while True:
            # Step 1.
            next1 = next
            next -= 1
            if pred(seq[next], seq[next1]) < 0:
                # Step 2.
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                # Step 3.
                reverse(seq, next1, last)
                # Change to yield references to get rid of
                # (at worst) |seq|! copy operations.
                yield seq[:]
                break
            if next == first:
                raise StopIteration
    raise StopIteration

def can_be_added(knotenliste, knoten):
    for knoten_tmp in knotenliste:
        summe = 0
        for pos in xrange(0,17):
            summe += (knoten_tmp[pos] and knoten[pos])
        if summe > 1:
            #print knotenliste
            #print knoten_tmp
            #print knoten
            return False
    return True
            
all_3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]
all_4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
all_5 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]
all_6 = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]

knotenliste = [[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]]
i = 0

punkte = 0
length = 0

"""for knoten in next_permutation(all_6):
    i += 1
    if can_be_added(knotenliste, knoten) and (len(knotenliste) < 2):
        knotenliste.append(knoten)
"""
punkte += (len(knotenliste) - length)*6
length = len(knotenliste)

for knoten in next_permutation(all_5):
    i += 1
    if can_be_added(knotenliste, knoten) and (len(knotenliste) < 5):
        knotenliste.append(knoten)

punkte += (len(knotenliste) - length)*5
length = len(knotenliste)

for knoten in next_permutation(all_4):
    i += 1
    if can_be_added(knotenliste, knoten):
        knotenliste.append(knoten)

punkte += (len(knotenliste) - length)*4
length = len(knotenliste)

for knoten in next_permutation(all_3):
    i += 1
    if can_be_added(knotenliste, knoten):
        knotenliste.append(knoten)

punkte += (len(knotenliste) - length)*3
length = len(knotenliste)

if length > 17:
    punkte -= 3*(len(knotenliste)-17)

print punkte
