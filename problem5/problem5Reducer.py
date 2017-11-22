#!/usr/bin/env python

import sys

code2ID = {}

for line in sys.stdin:
        line = line.strip()
        code,ID = line.split('\t',1)
        try:
                if code not in code2ID:
                        code2ID[code] = ID
                else:
                        pass
        except ValueError:
                pass
for code in code2ID:
        print code
