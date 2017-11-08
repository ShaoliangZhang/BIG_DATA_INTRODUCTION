#!/usr/bin/env python
import sys

person2friendcount = {}

for line in sys.stdin:
    line = line.strip()
    person, friend = line.split('\t', 1)
    try:
        if person not in person2friendcount:
		person2friendcount[person] = {}
	person2friendcount[person].setdefault(friend,0)
	person2friendcount[person][friend] = person2friendcount[person][friend] + 1
		
    except ValueError:
        pass

for person in person2friendcount:
	asymfriends = filter(lambda x : person2friendcount[person][x] == 1, person2friendcount[person].keys())
	for friend in asymfriends:
		print '%s\t%s' % (person,friend) 
