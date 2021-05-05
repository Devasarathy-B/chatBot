import name
import video
import speech


bot = 'LAKMÉ : {0}'
user ='USER  : {0}'


def intro():
    print(bot.format('WELCOME !!! TO \"SRI ESHWAR COLLEGE OF ENGINEERING\"'))
    speech.speech('WELCOME !!! TO \"SRI ESHWAR COLLEGE OF ENGINEERING\"')
    video.video()
    print(bot.format('MYSELF LAKMÉ, AN AUTOMATED MESSAGING CHATBOT'))
    speech.speech('MYSELF LAKMÉ, AN AUTOMATED MESSAGING CHATBOT')
    print(bot.format('WHAT IS YOUR NAME?'))
    speech.speech('WHAT IS YOUR NAME')
    name.name(input('USER  :'))
    print(bot.format('YOU CAN CLEAR YOUR DOUBT\'S WITH ME.......'))
    speech.speech('YOU CAN CLEAR YOUR DOUBT\'S WITH ME.......')
