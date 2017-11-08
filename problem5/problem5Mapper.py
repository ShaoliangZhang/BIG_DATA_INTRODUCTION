#!/usr/bin/env python
import sys
import json
 
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()

	# parse the line with json method
	dnaseq = json.loads(line)
	seqId = dnaseq[0]
	nucleotide = dnaseq[1]
	trimmedNucleotide = nucleotide[:-10]
	print '%s\t%s' % (trimmedNucleotide, seqId)
