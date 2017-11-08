#!usr/bin/env python
import sys

code2id = {}

for line in sys.stdin:
	line = strip()
	ID,code = line.split('\t',1)
	try:
		if code not in id2code:
			id2code[code] = ID
		else:
			pass
	except ValueError:
		pass
for ID in code2ID:
	print ID
