#!/usr/bin/env python
import sys
import types
 
id2order = {}
id2line = {}
for line in sys.stdin:
	line = line.strip()
	ID, value = line.split('\t',1)
	value = value.strip("[ u'")
	value = value.strip("']")
	value = value.split("', u'")

	try:
		if ID not in id2order:
			id2order[ID] = []
		if ID not in id2line:
			id2line[ID] = []
		if value[0] == 'order':
			id2order[ID] = value
		if value[0] == 'line_item':
			id2line[ID].append(value)
	except ValueError:
		pass 
for ID in id2order:
	for line in id2line[ID]:
		print '%s' % (id2order[ID]+line)
