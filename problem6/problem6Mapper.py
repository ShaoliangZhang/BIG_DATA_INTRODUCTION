#!/usr/bin/env python
import sys
import json
 
for line in sys.stdin:
	MaxI = 10
	MaxJ = 10
	line = line.strip()

	record = json.loads(line)
	if record[0] == 'a':
		i = record[1]
		for j in range(MaxJ+1):
			print '%s\t%s\t%s\t%s\t%s\t%s' % (i,j,record[0],record[1],record[2],record[3])
	elif record[0] == 'b':
		j = record[2]
		for i in range(MaxI+1):
			print '%s\t%s\t%s\t%s\t%s\t%s' % (i,j,record[0],record[1],record[2],record[3])
	else:
		pass
