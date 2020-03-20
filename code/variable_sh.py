import os
import pygame


firstpath = os.getcwd()
image_Path = os.path.join(firstpath,'image')
file_Path = os.path.join(firstpath,'file')
font_Path = os.path.join(firstpath,'file','font')
word_Path = os.path.join(firstpath,'file','wordfile')
wordlist_Path = os.path.join(firstpath,'file','wordlist')
Myfont = 'NanumBarunGothic.ttf'
WHITE = (255,255,255)
BLACK = (0,0,0)
pad_width = 1024
pad_height = 680
back_function = 0
cursortime = 0
shifttime = 0
searchword =""
typed = False
shifted = False
numpointlist = ['1.','2.','3.','4.','5.','6.']
page = 0

clock = pygame.time.Clock()
bookmarklist = []
