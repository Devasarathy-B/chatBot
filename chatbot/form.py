import speech
bot = 'LAKMÉ : {0}'

def form(n):
    print('**********************ADMISSION FORM*********************************')
    speech.speech('KINDLY FILL THE ADMISSION FORM')

    f=open(n+'.txt','w+')

    f.writelines('**********************ADMISSION FORM*********************************')

    print('ENTER YOUR FULL NAME : ')
    speech.speech('ENTER YOUR NAME')
    s=input('USER  : ')
    f.writelines('\nNAME : '+s)

    print('ENTER DOB : ')
    speech.speech('ENTER YOUR BIRTH DATE')
    s=input('USER  : ')
    f.writelines('\nDOB : '+s)

    print('ENTER YOUR GENDER : ')
    speech.speech('ENTER YOUR GENDER')
    s=input('USER  : ')
    f.writelines('\nGENDER : '+s)

    print('ENTER YOUR FATHER\'S NAME : ')
    speech.speech('ENTER YOUR FATHER\'S NAME')
    s=input('USER  : ')
    f.writelines('\nFATHER\'SNAME : '+s)

    print('ENTER YOUR ADDRESS : ')
    speech.speech('ENTER YOUR ADDRESS')
    s=input('USER  : ')
    f.writelines('\nADDRESS : '+s)

    print('ENTER YOUR MOBILE NUMBER : ')
    speech.speech('ENTER YOUR MOBILE NUMBER')
    s=input('USER  : ')
    f.writelines('\nMOBILE NUMBER : '+s)

    print('ENTER YOUR FATHER\'S MOBILE NUMBER : ')
    speech.speech('ENTER YOUR FATHER\'S MOBILE NUMBER')
    s=input('USER  : ')
    f.writelines('\nFATHER MOBILE NUMBER : '+s)

    print('ENTER YOUR MAIL ADDRESS : ')
    speech.speech('ENTER YOUR MAIL ADDRESS')
    s=input('USER  : ')
    f.writelines('\nMAIL ADDRESS : '+s)

    print('COUSE YOU ARE WILLING TO TAKE(CSE / ECE / EEE / MECH ) : ')
    speech.speech('COUSE YOU ARE WILLING TO TAKE(CSE / ECE / EEE / MECH ) : ')
    s=input('USER  : ')
    f.writelines('\nCOURSE : '+s)

    f=open(n+'.txt','r+')
    f1=f.readlines()
    for x in f1:
                  x=x.upper()
                  print(x)  
    f.close()
    print (bot.format('APPLICATION FILLED SUCCESSFULLY...............'))
    speech.speech('APPLICATION FILLED SUCCESSFULLY...............')

