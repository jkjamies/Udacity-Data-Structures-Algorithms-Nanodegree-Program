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
    possible_telemarketing_call = (
        filter_numbers_made_call_but_not_received(
            calls))
    possible_telemarketing_call = (
        filter_numbers_made_call_but_not_send_or_receive_text(
            possible_telemarketing_call
        ))

    possible_telemarketers = []
    for possible_telemarketer in possible_telemarketing_call:
        if possible_telemarketer[0] not in possible_telemarketers:
            possible_telemarketers.append(possible_telemarketer[0])

    return possible_telemarketers


def filter_numbers_made_call_but_not_received(possible_telemarketers):
    return [call for call in possible_telemarketers if call[1] not in call[0]]


def filter_numbers_made_call_but_not_send_or_receive_text(
        possible_telemarketers):
    text0_set = {text[0] for text in texts}
    text1_set = {text[1] for text in texts}
    return [
        call for call in possible_telemarketers
        if call[0] not in text0_set and call[0] not in text1_set
    ]


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
