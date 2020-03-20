def changekorean(alpha, shift = False):
   noShift = {'a':'ㅁ', 'b':'ㅠ','c':'ㅊ','d':'ㅇ','e':'ㄷ','f':'ㄹ','g':'ㅎ','h':'ㅗ','i':'ㅑ',
         'j':'ㅓ','k':'ㅏ','l':'ㅣ','m':'ㅡ','n':'ㅜ','o':'ㅐ','p':'ㅔ','q':'ㅂ','r':'ㄱ',
         's':'ㄴ','t':'ㅅ','u':'ㅕ','v':'ㅍ','w':'ㅈ','x':'ㅌ','y':'ㅛ','z':'ㅋ'}
   shifted = {'q':'ㅃ','w':'ㅉ','e':'ㄸ','r':'ㄲ','t':'ㅆ','o':'ㅒ','p':'ㅖ'}
   if (shift == True) and (alpha in shifted):
      return shifted[alpha]
   else:
      return noShift[alpha]

def conplusvowel(str):
	num = 0
	if str[0] == 'ㄱ':
		num += 44032
	elif str[0] == 'ㄲ':
		num += 44620
	elif str[0] == 'ㄴ':
		num += 45208
	elif str[0] == 'ㄷ':
		num += 45796
	elif str[0] == 'ㄸ':
		num += 46384
	elif str[0] == 'ㄹ':
		num += 46972
	elif str[0] == 'ㅁ':
		num += 47560
	elif str[0] == 'ㅂ':
		num += 48148
	elif str[0] == 'ㅃ':
		num += 48736
	elif str[0] == 'ㅅ':
		num += 49324
	elif str[0] == 'ㅆ':
		num += 49912
	elif str[0] == 'ㅇ':
		num += 50500
	elif str[0] == 'ㅈ':
		num += 51088
	elif str[0] == 'ㅉ':
		num += 51676
	elif str[0] == 'ㅊ':
		num += 52264
	elif str[0] == 'ㅋ':
		num += 52852
	elif str[0] == 'ㅌ':
		num += 53440
	elif str[0] == 'ㅍ':
		num += 54028
	elif str[0] == 'ㅎ':
		num += 54616
	elif str[0] == '':
		num += 55204
	if str[1] == 'ㅐ':
		num += 28*1
	elif str[1] == 'ㅑ':
		num += 28*2
	elif str[1] == 'ㅒ':
		num += 28*3
	elif str[1] == 'ㅓ':
		num += 28*4
	elif str[1] == 'ㅔ':
		num += 28*5
	elif str[1] == 'ㅕ':
		num += 28*6
	elif str[1] == 'ㅖ':
		num += 28*7
	elif str[1] == 'ㅗ':
		num += 28*8
	elif str[1] == 'ㅘ':
		num += 28*9
	elif str[1] == 'ㅙ':
		num += 28*10
	elif str[1] == 'ㅚ':
		num += 28*11
	elif str[1] == 'ㅛ':
		num += 28*12
	elif str[1] == 'ㅜ':
		num += 28*13
	elif str[1] == 'ㅝ':
		num += 28*14
	elif str[1] == 'ㅞ':
		num += 28*15
	elif str[1] == 'ㅟ':
		num += 28*16
	elif str[1] == 'ㅠ':
		num += 28*17
	elif str[1] == 'ㅡ':
		num += 28*18
	elif str[1] == 'ㅢ':
		num += 28*19
	elif str[1] == 'ㅣ':
		num += 28*20
	if 3 <= len(str):
		if str[2] == 'ㄱ':
			num += 1
		elif str[2] == 'ㄲ':
			num += 2
		elif str[2] == 'ㄳ':
			num += 3
		elif str[2] == 'ㄴ':
			num += 4
		elif str[2] == 'ㄵ':
			num += 5
		elif str[2] == 'ㄶ':
			num += 6
		elif str[2] == 'ㄷ':
			num += 7
		elif str[2] == 'ㄹ':
			num += 8
		elif str[2] == 'ㄺ':
			num += 9
		elif str[2] == 'ㄻ':
			num += 10
		elif str[2] == 'ㄼ':
			num += 11
		elif str[2] == 'ㄽ':
			num += 12
		elif str[2] == 'ㄾ':
			num += 13
		elif str[2] == 'ㄿ':
			num += 14
		elif str[2] == 'ㅀ':
			num += 15
		elif str[2] == 'ㅁ':
			num += 16
		elif str[2] == 'ㅂ':
			num += 17
		elif str[2] == 'ㅄ':
			num += 18
		elif str[2] == 'ㅅ':
			num += 19
		elif str[2] == 'ㅆ':
			num += 20
		elif str[2] == 'ㅇ':
			num += 21
		elif str[2] == 'ㅈ':
			num += 22
		elif str[2] == 'ㅊ':
			num += 23
		elif str[2] == 'ㅋ':
			num += 24
		elif str[2] == 'ㅌ':
			num += 25
		elif str[2] == 'ㅍ':
			num += 26
		elif str[2] == 'ㅎ':
			num += 27
	result = chr(num)
	if 4 <= len(str):
		result += str[4:]
	return result

def completeHangle(alpha):
	consonant = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㅃ','ㅉ','ㄸ','ㅆ']
	vowel = ['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅐ','ㅔ','ㅒ','ㅖ','ㅟ','ㅝ','ㅞ','ㅚ','ㅘ','ㅙ','ㅢ']
	concompo = {('ㄱ','ㅅ'):'ㄳ',('ㄴ','ㅈ'):'ㄵ',('ㄴ','ㅎ'):'ㄶ',('ㄹ','ㅂ'):'ㄼ',('ㄹ','ㅅ'):'ㄽ',('ㄹ','ㅌ'):'ㄾ',('ㄹ','ㅎ'):'ㅀ',('ㄹ','ㄱ'):'ㄺ',('ㄹ','ㅁ'):'ㄻ',
				('ㄹ','ㅍ'):'ㄿ',('ㅂ','ㅅ'):'ㅄ'}
	vocompo = {('ㅗ','ㅣ'):'ㅚ',('ㅗ','ㅏ'):'ㅘ',('ㅗ','ㅐ'):'ㅙ',('ㅜ','ㅣ'):'ㅟ',('ㅜ','ㅓ'):'ㅝ',('ㅜ','ㅔ'):'ㅞ',('ㅡ','ㅣ'):'ㅢ'}
	savealpha = ""
	for i in range(len(alpha)):
		if i == (len(alpha)-1) and (alpha[i-1],alpha[i]) not in vocompo:
			savealpha += alpha[i]
		elif 0 < i and (alpha[i-1],alpha[i]) in vocompo:
			continue
		elif (alpha[i],alpha[i+1]) in vocompo:
			savealpha += vocompo[(alpha[i],alpha[i+1])]
		else:
			savealpha += alpha[i]
	vowellist = []
	for i in range(len(savealpha)):
		if savealpha[i] in vowel:
			vowellist += [i]
	savealpha = ""
	for i in range(len(alpha)):
		if i == (len(alpha)-1) and (alpha[i-1],alpha[i]) not in concompo:
			savealpha += alpha[i]
		elif 0 < i and (alpha[i-1],alpha[i]) in concompo:
			continue
		elif (alpha[i],alpha[i+1]) in concompo:
			savealpha += concompo[(alpha[i],alpha[i+1])]
		else:
			savealpha += alpha[i]
	if vowellist == []:
		return savealpha
	vowellist = []
	for i in range(len(savealpha)):
		if savealpha[i] in vowel:
			vowellist += [i]
	result = ""
	if len(vowellist) == 1:
		if vowellist[0] == 0:
			result += savealpha
		elif 0 < vowellist[0]:
			result += conplusvowel(savealpha)
	elif 1 < len(vowellist):
		if vowellist[0] == 0:
			result += savealpha[:vowellist[1]-1]
		elif 0 < vowellist[0]:
			result += conplusvowel(savealpha[:vowellist[1]-1])
	for i in range(1,len(vowellist)-1):
		if vowellist[i]+1 < vowellist[i+1]:
			result += conplusvowel(savealpha[vowellist[i]-1:vowellist[i+1]-1])
		elif vowellist[i]+1 == vowellist[i+1]:
			result += savealpha[vowellist[i]:vowellist[i+1]-1]
	if 1 < len(vowellist):
		if vowellist[-2]+1 < vowellist[-1]:
			result += conplusvowel(savealpha[vowellist[-1]-1:])
		elif vowellist[-2]+1 == vowellist[-1]:
			result += savealpha[vowellist[-1]:]
	
	return result