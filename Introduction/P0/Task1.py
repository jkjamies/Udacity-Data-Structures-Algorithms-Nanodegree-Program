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


def get_unique_numbers_from_calls():
    unique_numbers = set()

    for call in calls:
        unique_numbers.add(call[0])
        unique_numbers.add(call[1])

    for text in texts:
        unique_numbers.add(text[0])
        unique_numbers.add(text[1])

    return unique_numbers


print('There are {} different telephone numbers in the records.'
      .format(len(get_unique_numbers_from_calls()))
      )

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
