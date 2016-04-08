print('------------------------------')
with open('quiz.txt') as txtfl:
	for line in txtfl:
		line = line.strip()
		print(line)
print('------------------------------')