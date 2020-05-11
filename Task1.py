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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


removed = 0
texts0 = []
texts1 = []
calls0 = []
calls1 = []

for entry in texts:
    texts0.append(entry[0])
    texts1.append(entry[1])

for entry in calls:
    calls0.append(entry[0])
    calls1.append(entry[1])

for entry in texts0:
    if entry in texts1:
        removed += 1
        texts0.remove(entry)

for entry in texts0:
    if entry in calls0:
        removed += 1
        texts0.remove(entry)

for entry in texts0:
    if entry in calls1:
        removed += 1
        texts0.remove(entry)


count = len(texts0) + removed

print("There are " + str(count) + " different telephone numbers in the records.")
