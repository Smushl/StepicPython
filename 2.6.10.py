a = []
while True:
    row = input().split()
    if row[0] == "end":
        break
    for j in range(len(row)):
        row[j] = int(row[j])
    a.append(row)
y = len(a[0])
x = len(a)
for i in range(len(a)):
    for j in range(len(a[0])):
        sum = a[i-1][j] + a[(i+1)%x][j] + a[i][j-1] + a[i][(j+1)%y]
        print(sum, end = " ")
    print()


