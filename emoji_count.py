import json

filenames = [""]

channels = {}


def get_count(message, chain, pointer):
        if ':)' not in message['message'] and !message['user']['turbo']:
            return 0
        
        user = message['user']['username']

        for i in range(0, 10):
            if ':)' in chain[pointer]['message'] and chain[pointer]['user']['username'] != user:
                return 1

            pointer += 1
            
    
for file in filename:
    pointer = 0
    log = json.loads(open(file), 'r')

    for message in json:
        pointer += 1
        if message[channel] not in channels:
            channels[channel] = 0

        channels[channel] += get_count(message)



print(channels)
                        
