#!/usr/bin/env python
import sys
 
# maps words to their counts
keys2value = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()
 
    # parse the input we got from mapper.py
	i,j,record = line.split('\t', 2)
	key = (i,j)
	record = record.split('\t')
    # convert count (currently a string) to int
	try:
		if key not in keys2value:
			keys2value[key] = []
		keys2value[key].append(record)
	#	print key,keys2value[key]
	except ValueError:
		pass

# write the results to STDOUT (standard output)
for key in keys2value:
	values = keys2value[key]
	a_rows = filter(lambda x : x[0] == 'a', values)
	b_rows = filter(lambda x : x[0] == 'b', values)
	
	result = 0
	for a in a_rows:
		for b in b_rows:
			if (a[2]==b[1]):
				result += int(a[3]) * int(b[3])

  # emit non-zero results
	if (result != 0):
		print '%s\t%s'%(key, result) 
