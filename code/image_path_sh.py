import os
import pygame


from variable_sh import *

os.chdir(image_Path)

#for filename in glob.glob(image_Path):
#    name, ext=os.path.splitext(filename)


#name=pygame.image.load(filename)

start_screen = pygame.image.load('startscreen.png')
background = pygame.image.load('background.png')
list_background = pygame.image.load('list_background.png')
word_background = pygame.image.load('word_background.png')
word_fullbackground = pygame.image.load('word_background.png')
	