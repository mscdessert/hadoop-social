#!/usr/bin/env python

from operator import itemgetter
import sys

current_device = None
current_count = 0
device = None

for line in sys.stdin:
    line = line.strip()

    words = line.split('\t')
    device = words[0]
    count = int(words[1])

    if current_device == device:
	current_count += count
    else:
	if current_device:
	    print '%s\t%s' % (current_device,current_count)
        current_count = count
	current_device = device

if current_device == device:
	    print '%s\t%s' % (current_device,current_count)
