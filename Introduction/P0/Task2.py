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


def combine_phone_time():
    phone_time = {}
    for call in calls:
        if call[0] not in phone_time:
            phone_time[call[0]] = int(call[3])
        else:
            phone_time[call[0]] += int(call[3])
        if call[1] not in phone_time:
            phone_time[call[1]] = int(call[3])
        else:
            phone_time[call[1]] += int(call[3])

    return (max(phone_time, key=phone_time.get),
            max(phone_time.values()))


ans = combine_phone_time()
print(
    '{} spent the longest time, {} seconds, on the phone during September 2016.'
    .format(ans[0], ans[1])
)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
