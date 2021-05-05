import cv2
import os
import form
import speech
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


bot = 'LAKMÉ : {0}'


def capture(n):
    
    cap = cv2.VideoCapture(0)
    print(bot.format('ENTER \"q\" TO CAPTURE AND SAVE'))
    speech.speech('ENTER \"q\" TO CAPTURE AND SAVE')
    while True:
        return_value,image = cap.read()
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow('image',gray)
        if cv2.waitKey(1)& 0xFF == ord('q'):
            cv2.imwrite('pic_'+n+'.jpg',image)
            break
    cap.release()
    cv2.destroyAllWindows()
    imgplot = plt.imshow(mpimg.imread('pic_'+n+'.jpg'))
    plt.show()
    print(bot.format('PHOTO SAVED SUCCESSFULLY...........'))
    speech.speech('PHOTO SAVED SUCCESSFULLY...........')
    form.form(n)
