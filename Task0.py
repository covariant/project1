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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

incoming_number1 = texts[0][0]
answering_number1 = texts[0][1]
t1 = texts[0][2]

incoming_number2 = calls[-1][0]
answering_number2 = calls[-1][1]
t2 = calls[-1][2]

print("First record of texts, " + str(incoming_number1) + " texts " + str(answering_number1) + " at time " + str(t1))
print("Last record of calls, " + str(incoming_number2) + " calls " + str(answering_number2) + " at time " + str(t2))
