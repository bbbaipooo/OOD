class TorKham:

	def __init__(self):
		self.words = []

	def restart(self):
		self.words = []
		return "game restarted"
#**********************
	def play(self, word):
		for self.i in self.words:
			if self.i == word:
				return "a game over"
		self.words.append(word)
		self.temp = self.words[len(self.words)-2]
		if len(self.words) == 1:
			return str(self.words)
		elif self.temp[len(self.temp)-2].lower()==word[0].lower() and self.temp[len(self.temp)-1].lower()==word[1].lower():
			return str(self.words)
		else:
			return "game over"
#********************

torkham = TorKham()
print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')

for i in S: #i is list of S         ex.banana,apple
    if i[0]=='R': # สมมุติวนอยู่ที่ลูปbanana i[0]=b
        print(torkham.restart())

    elif i[0]=='P':
        label,temp=i.split()
        print('\''+temp+'\' -> '+torkham.play(temp))

    elif i[0]=='X':
        break

    else:
        print('\''+i+'\' is Invalid Input !!!')
        break

