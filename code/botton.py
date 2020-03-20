import os
import pygame
from variable_sh import *

screen = pygame.display.set_mode((pad_width,pad_height))

class Button:
   
	def __init__(self, coord,imageFileName,imageFilePath = image_Path):
		self.coord = (coord[0],coord[1])
		os.chdir(imageFilePath)
		try:
			self.img = pygame.image.load(imageFileName)
		except pygame.error:
			print("해당 이미지를 불러올 수 없습니다.")
   
	def click(self):
		return self.img.get_rect(x=self.coord[0],y=self.coord[1]).collidepoint(pygame.mouse.get_pos())
      
	def show(self):

		try:
			screen.blit(self.img,self.coord)
		except AttributeError:
			print("해당 이미지를 불러오지 못해 화면에 표시할 수 없습니다.")
