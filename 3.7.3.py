n = int(input())
b, c = set(), set()
for i in range (n):
    b.add(input().lower().strip())
n = int(input())
for i in range (n):
    c.update(set(i.lower() for i in input().split()))
for e in c.difference(b):
    print(e)