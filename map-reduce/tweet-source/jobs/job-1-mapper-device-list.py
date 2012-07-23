#!/usr/bin/env python

import sys

#input comes from STDIN (standard input)
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()
    #split the line into words
    #print line
    words = line.split()
    #file identifier
    if words and words[0].strip() == 'INFO:':
        #print '%s\t1-tone-word-list\t%s' % (words[0].lower(), words[1].lower())
        parts = line.partition(' via ')
	if parts[2].strip():
            print '%s\t1' % (parts[2].strip())



#line = 'INFO: Roshan RTM via Mobile App'

#parts = line.partition('via')

#print parts[0]
#print parts[1]
#print parts[2].strip()
