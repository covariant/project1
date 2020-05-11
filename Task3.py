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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

i = 0
j = 0
removed = 0
calls0 = []
calls1 = []
mobiles_orig = []
mobiles = []
fixed = 0

for entry in calls:
    calls0.append(entry[0])
    calls1.append(entry[1])
    
for rec in calls1:
    if calls0[j][0:5] == '(080)':
        if rec[0:2] == '(0':
            mobiles_orig.append(rec[1:4])
        if rec[5] == ' ':
            mobiles_orig.append(rec[0:4])
            i += 1
        if rec[0:5] == '(080)':
            fixed += 1
    j += 1

for i in mobiles_orig:
    if i not in mobiles:
        mobiles.append(i)
        
list.sort(mobiles)
print(*mobiles, sep = "\n")

percentage = fixed / len(calls0)


print("\n{:.2f}".format(percentage * 100) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")