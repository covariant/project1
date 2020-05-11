"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

i = 0
j = 0
removed = 0
texts0 = []
texts1 = []
calls0 = []
calls1 = []
tele_orig = []
tele = []
fixed = 0

for entry in calls:
    texts0.append(entry[0])
    texts1.append(entry[1])

for entry in calls:
    calls0.append(entry[0])
    calls1.append(entry[1])

for entry in calls0:
    if entry not in calls1 or texts0 or texts1:
            tele_orig.append(entry)
        # if entry not in texts0:
        #     if entry not in texts1:

for i in tele_orig:
    if i not in tele:
        tele.append(i)

list.sort(tele)
print(*tele, sep = "\n")

