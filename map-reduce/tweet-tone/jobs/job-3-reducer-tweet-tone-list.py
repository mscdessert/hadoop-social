#!/usr/bin/env python

import sys

current_word = None
current_tone = None
current_count = None
previous_word = None
first_line_flag = True

#input comes from STDIN

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split('\t')
    current_word = words[0]

    if words[1] == '1-tone-word-list':
    	current_tone = words[2]
    else:
	current_count = words[2]
	
    if first_line_flag:
	first_line_flag = False
	previous_word = current_word
	continue
    else:
    	if previous_word == current_word:
	    print '%s\t%s' % (current_tone,current_count)
	else:
	    previous_word = current_word
