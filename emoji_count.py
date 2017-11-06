import json

log = json.loads(open('chatlogs.txt'), 'r')


channels = {}

for message in json:

    if message[channel] not in channels:
        channels[channel] = {'in': 0, 'out': 0}

    count = get_count(message)

    if count == 'in':
        channels[channel]['in'] += 1
    elif count == 'out':
        channels[channel]['out'] += 1


print(channels)
                    
