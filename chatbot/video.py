from moviepy.editor import *
import pygame
import time
def video():
    time.sleep(3)
    pygame.display.set_caption('SRI ESHWAR COLLEGE OF ENGINEERING')
    clip = VideoFileClip('SECE.mp4')
    clip.preview()
    pygame.quit()
  
