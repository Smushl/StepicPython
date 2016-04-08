a = int(input())
b = int(input())
c = 0;
num = 0
for i in range(a, b+1):
    if i % 3 == 0:
        c +=i
        num +=1
print(c / num)
