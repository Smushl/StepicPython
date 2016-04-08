n = int(input())
a = [[0]*n for i in range(n)]
r = 1
for k in range(n//2+1):
    x = n-k
    y = n-k
    j = 0+k
    i = 0+k
    while j < x:
        a[i][j] = r
        r +=1
        j +=1
    j -= 1
    i += 1
    while i < y:
        a[i][j] = r
        r +=1
        i +=1
    i -= 1
    j -= 1
    while j >= 0+k:
        a[i][j] = r
        r +=1
        j -=1
    j += 1
    i -= 1
    while i > 0+k:
        a[i][j] = r
        r +=1
        i -=1
for q in range(n):
    for w in range(n):
        print(a[q][w], end = " ")
    print()

