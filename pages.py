p1 = int(input('Введите первую страницу: '))
p2 = int(input('Введите последнюю страницу: '))
a = p1
while a <= p2:
    print(a, end=',')
    a += 2
a -= 1
print()
while a > p1:
	print(a, end=',')
	a -= 2
	