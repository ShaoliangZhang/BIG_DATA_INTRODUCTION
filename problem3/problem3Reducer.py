#!/usr/bin/env python

import sys
 
# maps words to their counts
name2count = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    name, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
        name2count[name] = name2count.get(name, 0) + count
    except ValueError:

        pass

# write the results to STDOUT (standard output)
for name in name2count:
	print '%s\t%s' % (name, name2count[name]) 
 
