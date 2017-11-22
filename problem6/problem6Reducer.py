#!/usr/bin/env python
import sys
 
keys2value = {}
 
for line in sys.stdin:
	line = line.strip()

	i,j,record = line.split('\t', 2)
	key = (i,j)
	record = record.split('\t')
	try:
		if key not in keys2value:
			keys2value[key] = []
		keys2value[key].append(record)
	except ValueError:
		pass

for key in keys2value:
	values = keys2value[key]
	a_rows = filter(lambda x : x[0] == 'a', values)
	b_rows = filter(lambda x : x[0] == 'b', values)
	
	result = 0
	for a in a_rows:
		for b in b_rows:
			if (a[2]==b[1]):
				result += int(a[3]) * int(b[3])

	if (result != 0):
		print '%s\t%s'%(key, result) 
