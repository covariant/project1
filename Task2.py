"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

duration = 0
tel = 0

for entry in calls:
    if int(entry[3]) > duration:
        duration = int(entry[3])
        tel = entry[0]

print(tel + " spent the longest time, " + str(duration + 10) + " seconds, on the phone during September 2016.")
        
