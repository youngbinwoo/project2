import os
import pygame
from variable_sh import *
from botton import *

grade_list = []
os.chdir(firstpath)
file = open("grade_list.txt",'r')
for lineContent in file:
	grade_list.append(lineContent.strip().split(','))
file.close()

	
def makewordtext(textfilename):
	for i in range(6):
		if textfilename[0] == grade_list[i+2][2]:
			wordnow_Path = os.path.join(word_Path,grade_list[i+2][4],textfilename[2])
			break
	os.chdir(wordnow_Path)
	wordtext = []
	try:
		with open(textfilename[2]+'.txt','r') as wordfile:
			for lineContent in wordfile:
				wordtext.append(lineContent.strip().split(','))
	except FileNotFoundError:
		print('해당단어의 txt파일이 없습니다.')
		return 0
   
	for j in range(len(wordtext)):
		for k in range(len(wordtext[j])):
			while "<c>" in wordtext[j][k]:
				index = wordtext[j][k].find("<c>")
				wordtext[j][k] = wordtext[j][k][:index] + "," + wordtext[j][k][index+3:]
         
			index = 0
			indexwhere = [0]
			
			while True:
				index += wordtext[j][k][index:].find("<n>")+3
				indexwhere += [index]
				if "<n>" not in wordtext[j][k][index:]:
					break
			indexwhere += [len(wordtext[j][k])+3]
			a = 0
			retext = []
			if "<n>" in wordtext[j][k]:
				for i in indexwhere:
					if i == 0:
						continue
					retext += [wordtext[j][k][a:i-3]]
					a = i
				wordtext[j][k] = retext
			else:
				wordtext[j][k] = [wordtext[j][k]]
			
	return wordtext