#!/usr/bin/python

import sys

itemTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the item type, val is the sale amount
#
# All the sales for a particular item will be presented,
# then the key will change and we'll be dealing with the next item
# Kamran Azmat

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisItem = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", itemTotal
        oldKey = thisKey;
        itemTotal = 0

    oldKey = thisKey
    itemTotal += float(thisItem)

if oldKey != None:
    print oldKey, "\t", itemTotal
