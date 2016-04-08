n = int(input())
x, y = 0, 0
for i in range(n):
    s = [i for i in input().split()]
    if s[0] == 'север': y += int(s[1])
    elif s[0] == 'юг': y -= int(s[1])
    elif s[0] == 'запад': x -= int(s[1])
    else: x += int(s[1]) #s[0] == 'восток'
print(x, y)