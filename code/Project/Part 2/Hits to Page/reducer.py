#!/usr/bin/python
# Kamran Azmat

import sys

pageHit = 0
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", pageHit
        oldKey = thisKey;
        pageHit = 0

    oldKey = thisKey
    pageHit += 1

if oldKey != None:
    print oldKey, "\t", pageHit
