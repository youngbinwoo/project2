import os
import pygame
from botton import *
from image_path_sh import *



back_button = Button((650,29),'back_button.png')
home_button = Button((700,29),'home_button.png')
search_button= Button((945,29),'search_button.png')
close_button = Button((680,310),'close_button.png')
right_popup = Button((75,290),'right_popup.png')
wrong_popup = Button((75,290),'wrong_popup.png')


def initGame():
	'''
	프로그램에서 사용하고자 하는 이미지들을 모두 불러온다.
	'''
	pygame.init()
	pygame.display.set_caption('doklibsimwha')
	os.chdir(image_Path)
	t=0
	while(t != 50):
		screen.blit(start_screen,(0,0))
		t += 1
		pygame.display.update()
		clock.tick(60)



