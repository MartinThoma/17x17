#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import deepcopy

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

def kantencheck(vector1, vector2):
    for pos, kugel in enumerate(vector1):
        if kugel == 1 and vector2[pos]:
            return False
    return True

def create_kanten(knoten):
    kantenliste = []
    for i in xrange(0, len(knoten)):
        for j in xrange(1, len(knoten)):
            if kantencheck(knoten[i], knoten[j]):
                #kantenliste.append(set([knoten[i], knoten[j]]))
                kantenliste.append(set([i, j]))
    return kantenliste

def is_clique(verticles, edges):
    """ This function returns True if the given verticles are in a clique. Else
        it returns False. 
        verticles is a list
        edges is a list of sets """
    nr_of_verticles = len(verticles)
    for key1 in xrange(0, nr_of_verticles - 1):
        for key2 in xrange(key1+1, nr_of_verticles):
            if set([verticles[key1], verticles[key2]]) not in edges:
                return False
    return True

def search_clique(nr_of_members,edges,verticles,list_of_verticles=[]):
    """ This function searches for one clique with exactly nr_of_members 
        verticles. When a clique is found, the list of verticles is returned.
        If no clique with this nr_of_members exists, none is returned. 
        list_of_verticles contains all verticles, that should be part of the
        clique. """
    if len(list_of_verticles) == nr_of_members:
        return list_of_verticles
    for verticle in verticles:
        if verticle not in list_of_verticles:
            new_list_of_verticles = deepcopy(list_of_verticles)
            new_list_of_verticles.append(verticle)
            if is_clique(new_list_of_verticles, edges):
                my_clique = search_clique(nr_of_members, edges, verticles, new_list_of_verticles)
                if my_clique:
                    return my_clique
    return False
    
print search_clique(3, [set([1,2]),set([2,3]),set([1,5]), set([4,5]), set([1,3])],[1,2,3,4,5])


all_4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
all_5 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]

knoten = []

"""for p in next_permutation(all_4):
    permutations.append(p)"""
for p in next_permutation(all_5):
    knoten.append(p)
print "Es wurden " + str(len(knoten)) + " Knoten erstellt."
kanten = create_kanten(knoten)
print "Es wurden " + str(len(kanten)) + " Kanten erstellt."
my_clique = search_clique(17, kanten, range( len(knoten) ) )
for node in my_clique:
    print knoten[node]

"""
print len(permutations)
print min(kanten)
print max(kanten)"""
