import intro
import speech
import capture
import respond 
import responses


bot = 'LAKMÉ : {0}'
user ='USER  : {0}'


intro.intro()

while True:
    message = input('USER  : ')
    message = message.lower()
    if message == 'exit':
        print(bot.format('DO YOU LIKE TO FILL ADMISSION FORM (y/n)'))
        speech.speech('DO YOU LIKE TO FILL ADMISSION FORM')
        a=input('USER  : ')
        if a == 'Y' or a == 'y':
            print('NAME PLEASE :')
            speech.speech('NAME PLEASE')
            r=input('USER  : ')
            capture.capture(r)
        print(bot.format('THANK YOU FOR SPENDING TIME WITH US (- | -)!!!'))
        speech.speech('THANK YOU FOR SPENDING TIME WITH US (- | -)!!!')
        break
    else:
        response = respond.receive_message(responses.responses,message)
        response = response.upper()
        print(bot.format(response))
        speech.speech(response)
        
