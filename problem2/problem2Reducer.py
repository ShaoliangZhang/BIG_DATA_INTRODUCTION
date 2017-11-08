#!/usr/bin/env python
import sys
import types
 
# maps words to their counts
id2order = {}
id2line = {}
# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	ID, value = line.split('\t',1)
	value = value.strip("[ u'")
	value = value.strip("']")
	value = value.split("', u'")

    # convert count (currently a string) to int
	try:
		if ID not in id2order:
			id2order[ID] = []
			id2line[ID] = []
		if value[0] == 'order':
			id2order[ID].append(value)
		if value[0] == 'line_item':
			id2line[ID].append(value)
	except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
		pass 

for ID in id2order:
	order = id2order[ID]
	for n in id2line[ID]:
		print '%s' % (order+n)
