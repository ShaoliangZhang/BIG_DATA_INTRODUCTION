#!/usr/bin/env python
import sys
import json
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()

	# parse the line with json method
	record = json.loads(line)
	fileName = record[0]
	value = record[1]

    # split the line into words
	words = value.split()

    # increase counters
	for w in words:
		print '%s\t%s' % (w, fileName)
