import re
import random



def receive_message(responses,message):
    response = respond(responses,message)
    return response



def respond(responses, message):
    response= random.choice(responses['default'])
    for pattern, reply in responses.items():
        match = re.search(pattern, message)
        if match is not None:
            response = random.choice(reply)
    return response
