#!/usr/bin/env python
import sys
import json
 
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()

	# parse the line with json method
	record = json.loads(line)
	print '%s\t%s' % (record[0],record[1])
	print '%s\t%s' % (record[1],record[0])
