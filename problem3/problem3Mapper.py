#!/usr/bin/env python
import sys
import json
 
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()

	# parse the line with json method
	record = json.loads(line)
	name = record[0]

	print '%s\t%s' % (name, 1)
