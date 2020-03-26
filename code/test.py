def first():
	print('hi')
	while(1):
		num = input("입력하세요 : ")
		if num == '1':
			break
	return second()

def second():
	print('hello')
	while(1):
		num = input("입력하세요 : ")
		if num == '2':
			break
	return third()

def third():
	print('bye')
	while(1):
		num = input("입력하세요 : ")
		if num == '3':
			break
		elif num == '0':
			exit()
	return first()
			
first()
		