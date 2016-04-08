a = [int(i) for i in input().split()]
sum = 0
if len(a) == 1:
        print(a[0])
else:
        for i in range(len(a)):
                sum = a[(i + 1)%len(a)] + a[i - 1]
                print(sum, end = " ")
