#!/usr/bin/env python

import sys
 
name2count = {}
 
for line in sys.stdin:
    line = line.strip()
 
    name, count = line.split('\t', 1)

    try:
        count = int(count)
        name2count[name] = name2count.get(name, 0) + count
    except ValueError:

        pass

for name in name2count:
	print '%s\t%s' % (name, name2count[name]) 
 
