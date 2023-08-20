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


def filter_out_telemarketers():
    numbers_making_calls = {call[0] for call in calls}
    numbers_receiving_calls = {call[1] for call in calls}
    numbers_sending_texts = {text[0] for text in texts}
    numbers_receiving_texts = {text[1] for text in texts}

    callers = numbers_making_calls

    numbers_to_avoid = (
        numbers_receiving_calls
        .union(numbers_sending_texts)
        .union(numbers_receiving_texts)
    )

    telemarketers = callers - numbers_to_avoid

    return telemarketers


print('These numbers could be telemarketers: ')
for number in sorted(filter_out_telemarketers()):
    print(number)

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
