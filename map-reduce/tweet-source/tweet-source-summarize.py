#!/usr/bin/python

import sys
import locale

# Read sorted input of device-summary-list - sort the list in descending order
# Keep track of the total number of tweets
# Keep track of number of tweets for N number of devices; take N as parameter

# Print total number of tweets
# Pring percentage of tweets through the N devices

try:
    N = int(sys.argv[1])
except  IndexError:
    N = 5
    pass

total_tweets = 0
device_summary_list = []
count = 0
percentage = 0.00

for line in sys.stdin:
    words = line.split('\t')
    count = count + 1
    if int(count) <= int(N) :
	device_details = {'name': words[0], 'tweet_count':int(words[1])}
	device_summary_list.append(device_details)

    total_tweets = total_tweets + int(words[1])

count = 0

locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

print '\n{0:3} ] {1:30} {2:10} {3:10}'.format('###','Source','Tweet count','% of TOTAL\n')

for device in device_summary_list:
    count = count + 1
    percentage = (float(device['tweet_count'])/float(total_tweets)) * 100
    #print '%s ] %s\t\t\t\t:Tweet count = %s : Percentage = %f' % (str(count),device['name'],device['tweet_count'],percentage)
    print '{0:3} ] {1:30} {2:10n} {3:10.4}'.format(count,device['name'],device['tweet_count'],percentage)

print '\nTOTAL no of Tweets = {0:10n}\n'.format(total_tweets)

