import os
import pygame
from variable_sh import *

screen = pygame.display.set_mode((pad_width,pad_height))

class Sentence:
   
	def __init__(self, coord, line, fontsize = 35, cut = False, color = (0,0,0)):
		self.coord = (coord[0],coord[1])
		self.line = line
		self.face = 0
		os.chdir(font_Path)
		if cut == False:
			fontObj = pygame.font.Font(Myfont, fontsize)
			textSurfaceObj = fontObj.render(line, True, color)
			textRectObj = textSurfaceObj.get_rect()
			textRectObj.center = coord
			self.face = textRectObj
			screen.blit(textSurfaceObj, textRectObj)
		else:
			fontObj = pygame.font.Font(Myfont, fontsize)
			textSurfaceObj = fontObj.render(line, True, color)
			textRectObj = textSurfaceObj.get_rect()
			textRectObj.topleft= coord
			self.face = textRectObj
			screen.blit(textSurfaceObj, textRectObj)
         
	def write(self,fontsize=50,font=Myfont,color=(0,0,0),mid=True):
		os.chdir(font_Path)
		fontObj = pygame.font.Font(font, fontsize)
		textSurfaceObj = fontObj.render(self.line, True, color)
		textRectObj = textSurfaceObj.get_rect()
		if mid == True:
			textRectObj.center = self.coord
		else:
			textRectObj= self.coord
		self.face = textRectObj
		screen.blit(textSurfaceObj, textRectObj)
   
	def click(self):
		return self.face.collidepoint(pygame.mouse.get_pos())