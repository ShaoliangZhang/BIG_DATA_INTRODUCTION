#!/usr/bin/env python
import sys
	 
# maps words to their counts
word2filelist = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()	
    # parse the input we got from mapper.py
    word, filename = line.split('\t',1)

    # convert count (currently a string) to int
    try:
	if word not in word2filelist:
		word2filelist[word] = []
	if filename not in word2filelist[word]:
		word2filelist[word].append(filename)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        pass

# write the results to STDOUT (standard output)
for word in word2filelist:
	print '%s\t%s' % (word, word2filelist[word]) 
 
