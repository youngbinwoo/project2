import pygame
import os
import hangle
from variable_sh import *
from image_path_sh import *
from botton import *
from sentence import *
from initGame import *
from makelist import *
from screenshow import *


screen = pygame.display.set_mode((pad_width,pad_height))
back_button = Button((650,29),'back_button.png')
home_button = Button((700,29),'home_button.png')
search_button= Button((945,29),'search_button.png')

os.chdir(file_Path)
if os.path.isfile('bookmark.txt'):
    file = open('bookmark.txt','r')
    for lineContent in file:
        bookmarklist.append(lineContent.strip().split(','))
    file.close()
    bookmarklist = bookmarklist[0][:-1]

def make_wordlist(grade,testword = ""):
	os.chdir(wordlist_Path)
	fileMatrix = []
	wordlist = []
	if grade == '검색':
		with open('allwordlist2.csv','r') as file:
			for word in file:
				fileMatrix.append(word.strip().split(','))
			for i in range(len(fileMatrix)-1):
				if testword in fileMatrix[i][0]:
					wordlist.append(fileMatrix[i][1:])
	else:
		with open('allwordlist.csv','r') as file:
			for word in file:
				fileMatrix.append(word.strip().split(','))
		for i in range(len(fileMatrix)-1):
			if grade == grade_list[0][0]:
				if fileMatrix[i][1] in bookmarklist:
					wordlist.append(fileMatrix[i])
			elif grade == grade_list[1][0]:
				wordlist.append(fileMatrix[i])
			else:
				for j in range(3):
					if grade == grade_list[j+2][0]:
						if fileMatrix[i][0] == grade_list[j+2][2] or fileMatrix[i][0] == grade_list[j+5][2]:
							wordlist.append(fileMatrix[i])
							break
	return wordlist

def bookmarktest(word,x,y):
	if word[1] in bookmarklist:
		return Button((x,y),'star_button2.png')
	return Button((x,y),'star_button.png')   

def word_search():
	global screen, clock, grade, cursortime, shifttime, searchword, typed, shifted, test, cursor
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
				shifted = True
				shifttime = cursortime
			if event.key == pygame.K_RETURN:
				typed = True
			elif event.unicode.isalpha() and shifted == True:
				searchword += hangle.changekorean(event.unicode,True)
			elif event.unicode.isalpha()and shifted == False:
				searchword += hangle.changekorean(event.unicode)
			elif event.key == pygame.K_BACKSPACE:
				searchword = searchword[:-1]
	if 15 <= cursortime <30:
		cursortime += 1
		cursor = "|"
	elif cursortime == 30:
		cursortime = 0
	else:
		cursortime += 1
		cursor = ""
	if shifttime == cursortime:
		shifted = False
	Sentence((780,35),hangle.completeHangle(searchword)+cursor,20,True)
	if typed == True:
		typed = False
		cursortime = 0
		shifttime = 0
		test = False
		word_list('검색',searchword)

def quiz(number):
	global screen, clock, tablist
	if wordtext == 0:
		word_list(grade)
	answer_cursortime = 0
	answer =""
	typed = False
	getanswer_button = Button((100,540),'getanswer_button.png')
	return_button = Button((565,540),'return_button.png')
	ATQcliked = False
	for i in range(6):
		if wordnow[0] == grade_list[i+2][2]:
			wordnow_Path = os.path.join(word_Path,grade_list[i+2][4],wordnow[2])
			break
	picture = Button((75,290),wordtext[number][3][0]+'.png',wordnow_Path)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.click():
					word_list(grade)
				elif home_button.click():
					startGame()
				elif close_button.click():
					typed = False
				elif ATQ.click():
					ATQcliked = True
				elif return_button.click():
					typed = True
				for i in range(len(wordtext)):
					if tablist[i].click():
						tablist[number] = Button((785,150+(62*number)),'tab_button2.png')
						tablist[i] = Button((785,150+(62*i)),'tab_button.png')
						worddetail(i)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typed = True
				elif event.unicode.isalpha() and not typed:
					answer += event.unicode
				elif event.unicode.isdigit() and not typed:
					answer += event.unicode
				elif event.key == pygame.K_BACKSPACE and not typed:
					answer = answer[:-1]
			elif event.type == pygame.QUIT:
				os.chdir(file_Path)
				file = open('bookmark.txt','w')
				for i in range(len(bookmarklist)):
					file.write(bookmarklist[i]+',')
				file.close()
				pygame.quit()
		if 15 <= answer_cursortime <30:
			answer_cursortime += 1
			answer_cursor = "|"
		elif answer_cursortime == 30:
			answer_cursortime = 0
		else:
			answer_cursortime += 1
			answer_cursor = ""
		screen.fill(WHITE)
		screen.blit(word_fullbackground,(0,0))
		back_button.show()
		home_button.show()
		search_button.show()
		getanswer_button.show()
		return_button.show()
		Sentence((116,205),wordtext[number][0][0],25,True)
		Sentence((675,174),wordnow[1],20)
		if ATQcliked:
			Sentence((110,555),answer+answer_cursor,20,True)
		elif answer == "":
			ATQ = Sentence((110,555),"정답을 입력해 주세요!",20,True)
		else:
			Sentence((110,555),answer+answer_cursor,20,True)
		for i in range(6):
			if wordnow[0] == grade_list[i+2][2]:
				Sentence((600,220),grade_list[i+2][3],20,True)
				break
		picture.show()
		for j in range(len(wordtext)):
			tablist[j].show()
			Sentence((900,178+(62*j)),wordtext[j][0][0],20)
		for j in range(len(xtablist)):
			(xtablist[j]).show()
			Sentence((900,178+(62*(len(wordtext)+j))),'-',20)
		if typed == True:
			if answer == wordtext[number][1][0]:
				right_popup.show()
			else:
				wrong_popup.show()
			close_button.show()
		pygame.display.update()
		clock.tick(60)

def worddetail(number):
	global screen, clock, tablist
	for i in range(6):
		if wordnow[0] == grade_list[i+2][2]:
			wordnow_Path = os.path.join(word_Path,grade_list[i+2][4],wordnow[2])
			break
	if 3<len(wordtext[number]):
		if wordtext[number][2][0] == '1':
			picture = Button((41,400),wordtext[number][3][0]+'.png',wordnow_Path)
		elif wordtext[number][2][0] == '2':
			picture = Button((390,260),wordtext[number][3][0]+'.png',wordnow_Path)
		elif wordtext[number][2][0] == '3':
			quiz(number)
	maxlength = 0
	for i in range(len(wordtext[number][1])):
		if wordtext[number][1][i][:2] in numpointlist:
			if maxlength < len(wordtext[number][1][i]):
				maxlength = len(wordtext[number][1][i])
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.click():
					word_list(grade)
				elif home_button.click():
					startGame()
				for i in range(len(wordtext)):
					if tablist[i].click():
						tablist[number] = Button((785,150+(62*number)),'tab_button2.png')
						tablist[i] = Button((785,150+(62*i)),'tab_button.png')
						worddetail(i)
			elif event.type == pygame.QUIT:
				os.chdir(file_Path)
				file = open('bookmark.txt','w')
				for i in range(len(bookmarklist)):
					file.write(bookmarklist[i]+',')
				file.close()
				pygame.quit()
      
		screen.fill(WHITE)
		screen.blit(word_fullbackground,(0,0))
		back_button.show()
		home_button.show()
		search_button.show()
		Sentence((116,205),wordtext[number][0][0],25,True)
		Sentence((675,174),wordnow[1],20)
		for i in range(6):
			if wordnow[0] == grade_list[i+2][2]:
				Sentence((595,215),grade_list[i+2][3],20,True)
				break
		if len(wordtext[number])<4:
			try:
				for i in range(len(wordtext[number][1])):
					if wordtext[number][1][i][:2] in numpointlist:
						Sentence((405-7.5*maxlength,435-20*len(wordtext[number][1])+(i*40)),wordtext[number][1][i],25,True)
					else:
						Sentence((405,450-20*len(wordtext[number][1])+(i*40)),wordtext[number][1][i],25)
			except IndexError:
				print("allwordlist.csv의 해당 단어 부분 확인.")
				worddata(wordnow)
		elif wordtext[number][2][0] == '1':
			picture.show()
			for i in range(len(wordtext[number][1])):
				if wordtext[number][1][i][:2] in numpointlist:
					Sentence((405-7.5*maxlength,355-20*len(wordtext[number][1])+(i*40)),wordtext[number][1][i],25,True)
				else:
					Sentence((405,370-20*len(wordtext[number][1])+(i*40)),wordtext[number][1][i],25)
		elif wordtext[number][2][0] == '2':
			picture.show()
			for i in range(len(wordtext[number][1])):
				if wordtext[number][1][i][:2] in numpointlist:
					Sentence((230-7.5*maxlength,455-20*len(wordtext[number][1])+(i*40)),wordtext[number][1][i],25,True)
				else:
					Sentence((230,470-20*len(wordtext[number][1])+(i*40)),wordtext[number][1][i],25)
		else:
			for i in range(len(wordtext[number][1])):
				if wordtext[number][1][i][:2] in numpointlist:
					Sentence((405-7.5*maxlength,435-20*len(wordtext[number][1])+(i*40)),wordtext[number][1][i],25,True)
				else:
					Sentence((405,450-20*len(wordtext[number][1])+(i*40)),wordtext[number][1][i],25)
					
		for j in range(len(wordtext)):
			tablist[j].show()
			Sentence((900,178+(62*j)),wordtext[j][0][0],20)
		for j in range(len(xtablist)):
			(xtablist[j]).show()
			Sentence((900,178+(62*(len(wordtext)+j))),'-',20)
		pygame.display.update()
		clock.tick(60)

def worddata(word):
	global screen, clock, wordtext, wordnow, tablist, xtablist
	wordnow = word
	wordtext = makewordtext(word)
	for i in range(6):
		if wordnow[0] == grade_list[i+2][2]:
			wordnow_Path = os.path.join(word_Path,grade_list[i+2][4],wordnow[2])
			break
	if wordtext == 0:
		word_list(grade)
	if 3<len(wordtext[0]):
		if wordtext[0][2][0] == '1':
			picture = Button((41,400),wordtext[0][3][0]+'.png',wordnow_Path)
		elif wordtext[0][2][0] == '2':
			picture = Button((390,260),wordtext[0][3][0]+'.png',wordnow_Path)
	tablist = [Button((785,150),'tab_button.png')]
	for i in range(1,len(wordtext)):
		tablist +=[Button((785,150+(62*i)),'tab_button2.png')]
	xtablist = []
	for i in range(0,8-len(wordtext)):
		xtablist +=[Button((785,150+(62*(len(wordtext)+i))),'tab_button2.png')]
	maxlength = 0
	for i in range(len(wordtext[0][1])):
		if maxlength < len(wordtext[0][1][i]):
			maxlength = len(wordtext[0][1][i])
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.click():
					word_list(grade)
				elif home_button.click():
					startGame()
				for i in range(1,len(wordtext)):
					if tablist[i].click():
						tablist[0] = Button((785,150),'tab_button2.png')
						tablist[i] = Button((785,150+(62*i)),'tab_button.png')
						worddetail(i)
			elif event.type == pygame.QUIT:
				os.chdir(file_Path)
				file = open('bookmark.txt','w')
				for i in range(len(bookmarklist)):
					file.write(bookmarklist[i]+',')
				file.close()
				pygame.quit()
      
		screen.fill(WHITE)
		screen.blit(word_background,(0,0))
		back_button.show()
		home_button.show()
		search_button.show()
		Sentence((120,205),word[1],25,True)
		Sentence((675,174),word[1],20)
		for i in range(6):
			if wordnow[0] == grade_list[i+2][2]:
				Sentence((595,215),grade_list[i+2][3],20,True)
				break
		try:
			if len(wordtext[0])<4:
				try:
					for i in range(len(wordtext[0][1])):
						if wordtext[0][1][i][:2] in numpointlist:
							Sentence((405-7.5*maxlength,435-20*len(wordtext[0][1])+(i*40)),wordtext[0][1][i],25,True)
						else:
							Sentence((405,450-20*len(wordtext[0][1])+(i*40)),wordtext[0][1][i],25)
				except IndexError:
					print("allwordlist.csv의 해당 단어 부분 확인.")
					worddata(wordnow)
			elif wordtext[0][2][0] == '1':
				picture.show()
				for i in range(len(wordtext[0][1])):
					if wordtext[0][1][i][:2] in numpointlist:
						Sentence((405-7.5*maxlength,355-20*len(wordtext[0][1])+(i*40)),wordtext[0][1][i],25,True)
					else:
						Sentence((405,370-20*len(wordtext[0][1])+(i*40)),wordtext[0][1][i],25)
			elif wordtext[0][2][0] == '2':
				picture.show()
				for i in range(len(wordtext[0][1])):
					if wordtext[0][1][i][:2] in numpointlist:
						Sentence((230-7.5*maxlength,455-20*len(wordtext[0][1])+(i*40)),wordtext[0][1][i],25,True)
					else:
						Sentence((230,470-20*len(wordtext[0][1])+(i*40)),wordtext[0][1][i],25)
			else:
				for i in range(len(wordtext[0][1])):
					if wordtext[0][1][i][:2] in numpointlist:
						Sentence((405-7.5*maxlength,435-20*len(wordtext[0][1])+(i*40)),wordtext[0][1][i],25,True)
					else:
						Sentence((405,450-20*len(wordtext[0][1])+(i*40)),wordtext[0][1][i],25)
		except IndexError:
			print('해당 단어의 txt파일을 확인하세요.')
			word_list(grade)
		for j in range(len(wordtext)):
			(tablist[j]).show()
			Sentence((900,178+(62*j)),wordtext[j][0][0],20)
		for j in range(len(xtablist)):
			(xtablist[j]).show()
			Sentence((900,178+(62*(len(wordtext)+j))),'-',20)
		pygame.display.update()
		clock.tick(60)

def word_list(grade,testword = ""):
	global screen,clock, bookmarklist, wordlist, wordlistnow, searchword,page
	left_button = Button((60,540),'left_page_button.png')
	right_button = Button((930,540),'right_page_button.png')
	searchword = ""
	wordnum = 18
	while True:
		screen.fill(WHITE)
		screen.blit(list_background,(0,0))
		for i in range(6):
			if grade == grade_list[i][0]:
				Sentence((200,149),grade_list[i][1],23)
		if grade == '검색':
			Sentence((200,149),hangle.completeHangle(testword),23)
		wordlist = make_wordlist(grade,testword)
		back_button.show()
		home_button.show()
		search_button.show()
		left_button.show()
		right_button.show()
	
		wordlistnow = []
		if page < ((len(wordlist))//wordnum):
			for i in range(wordnum):
				wordlistnow += [Sentence((130+(266*(i//6)),232+(66*(i%6))),wordlist[(page)*wordnum+i][1],20,True)]
				bookmarktest(wordlist[(page)*wordnum+i],300+(275*(i//6)),224+(66*(i%6))).show()
		elif page == ((len(wordlist))//wordnum):
			for i in range(len(wordlist)%wordnum):
				wordlistnow += [Sentence((130+(266*(i//6)),232+(65*(i%6))),wordlist[(page)*wordnum+i][1],20,True)]
				bookmarktest(wordlist[(page)*wordnum+i],300+(280*(i//6)),226+(66*(i%6))).show()
		
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.click():
					startGame()
				elif home_button.click():
					startGame()
				elif left_button.click():
					if page > 0:
						page -= 1
				elif right_button.click():
					if page < ((len(wordlist)//wordnum)):
						page += 1
				elif home_button.click():
					startGame()
				
				if page<(len(wordlist)//wordnum): 
					for i in range(len(wordlistnow)):
						if wordlistnow[i].click():
							return worddata(wordlist[(page*wordnum)+i])
						elif bookmarktest(wordlist[((page)*wordnum)+i],310+(266*(i//6)),224+(65*(i%6))).click():
							if wordlist[(page)*wordnum+i][1] not in bookmarklist:
								bookmarklist += [wordlist[(page)*wordnum+i][1]]
							elif wordlist[(page)*wordnum+i][1] in bookmarklist:
								bookmarklist.remove(wordlist[(page)*wordnum+i][1])
				elif page==(len(wordlist)//wordnum):
					for i in range(len(wordlist)%wordnum):
						if wordlistnow[i].click():
							worddata(wordlist[(page*wordnum)+i])
						elif bookmarktest(wordlist[((page)*wordnum)+i],310+(266*(i//6)),224+(65*(i%6))).click():
							if wordlist[(page)*wordnum+i][1] not in bookmarklist:
								bookmarklist += [wordlist[(page)*wordnum+i][1]]
							elif wordlist[(page)*wordnum+i][1] in bookmarklist:
								bookmarklist.remove(wordlist[(page)*wordnum+i][1])
			elif event.type == pygame.QUIT:
				os.chdir(file_Path)
				file = open('bookmark.txt','w')
				for i in range(len(bookmarklist)):
					file.write(bookmarklist[i]+',')
				file.close()
				pygame.quit()

		pygame.display.update()
		clock.tick(60)

def startGame():
	global screen, clock,start_screen, bookmarklist, grade, test,page
	os.chdir(image_Path)
	button_list = [Button((190,520),'bookmark_button.png'),
					Button((440,520),'wordall_button.png'),
					Button((150,300),'mid1_button.png'),
					Button((335,300),'mid2_button.png'),
					Button((520,300),'mid3_button.png')]
	test = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				for i in range(5):
					if button_list[i].click():
						grade = grade_list[i][0]
						page = 0
						return word_list(grade)
				if back_button.click():
					startGame()
				elif home_button.click():
					startGame()
				elif search_button.click():
					grade = '검색'
					test = True
			elif event.type == pygame.QUIT:
				os.chdir(file_Path)
				file = open('bookmark.txt','w')
				for i in range(len(bookmarklist)):
					file.write(bookmarklist[i]+',')
				file.close()
				pygame.quit()
		screen.fill(WHITE)
		screen.blit(background,(0,0))
		for i in range(5):
			button_list[i].show()
		search_button.show()
		back_button.show()
		home_button.show()
		if test == True:
			word_search()
		pygame.display.update()
		clock.tick(60)
        
	
initGame()
startGame()
