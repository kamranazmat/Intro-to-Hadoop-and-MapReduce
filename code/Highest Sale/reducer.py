#!/usr/bin/python

import sys

storeHighest = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
# Kamran Azmat

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, value = data_mapped
    value = float(value)
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", storeHighest
        oldKey = thisKey;
        storeHighest = 0

    oldKey = thisKey
    if value > storeHighest:
	storeHighest = value

if oldKey != None:
    print oldKey, "\t", storeHighest
