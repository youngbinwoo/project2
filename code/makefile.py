import os
import shutil
firstPath = os.getcwd()
wordnum = [56,39,16,17,16,15]
grade = ['11','12','21','22','31','32']
for j in range(6):
	os.chdir(os.path.join(firstPath,'mid'+grade[j]))
	file_list = os.listdir(os.path.join(firstPath,'mid'+grade[j]))
	file_list.sort()

	for i in range(1,wordnum[j]+1):
		YOUR_DIRECTORY_NAME = 'mid'+grade[j]+'_'+str(i)
		try:
			if not(os.path.isdir(YOUR_DIRECTORY_NAME)):
				os.makedirs(os.path.join(YOUR_DIRECTORY_NAME))
		except OSError as e:
			if e.errno != errno.EEXIST:
				print("Failed to create directory!!!!!")
				raise
	for i in range(1,wordnum[j]+1):
		try:
			shutil.move('mid'+grade[j]+'_'+str(i)+'.txt', 'mid'+grade[j]+'_'+str(i))
		except:
			print("check"+grade[j]+'_'+str(i)+'.txt')
		for item in file_list:
			try:
				if item.find('mid'+grade[j]+'_'+str(i)+'_') is not -1:
					shutil.move(item,'mid'+grade[j]+'_'+str(i))
			except:
				print("check"+'mid'+grade[j]+'_'+str(i))