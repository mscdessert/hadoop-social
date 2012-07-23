#!/usr/bin/env python

import sys

strip_list='[].?'

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    if words and words[0]=='INFO:':
	continue
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
	word = word.strip(strip_list)
	if word == '':
	    continue
        print '%s\t%s' % (word.lower(), 1)


