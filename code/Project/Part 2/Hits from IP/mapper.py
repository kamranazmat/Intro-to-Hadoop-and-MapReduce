#!/usr/bin/python

# Format of each line is:
# Common Log Format
#
# We want element 5 (request)
# We need to write them out to standard output, separated by a tab
# Kamran Azmat

import sys, re

p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) != 10:
	continue
    else:	
	m = p.match(line)
	if not m:
            continue
	host, ignore, user, date, request, status, size = m.groups()
	
	print host.strip("[|]'")
