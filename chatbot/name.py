import random
import speech

bot = 'LAKMÉ : {0}'


def name(message):
    n = message
    names={1:['hello,{0}!'.format(n),
            'sweet name {0}!'.format(n),
              'it\'s my pleasure to meet you {0}'.format(n)]
           }
    namee = random.choice(names[1])
    namee = namee.upper()
    print(bot.format(namee))
    speech.speech(namee)
