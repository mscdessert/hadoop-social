#!/usr/bin/env python

from operator import itemgetter
import sys

current_tone = None
current_count = 0
tone = None

for line in sys.stdin:
    line = line.strip()

    words = line.split()
    tone = words[0]
    count = int(words[1])

    if current_tone == tone:
	current_count += count
    else:
	if current_tone:
	    print '%s\t%s' % (current_tone,current_count)
        current_count = count
	current_tone = tone

if current_tone == tone:
	    print '%s\t%s' % (current_tone,current_count)
