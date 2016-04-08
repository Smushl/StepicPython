a = [int(i) for i in input().split()]
i = int(input())
p = False
for j in range(len(a)):
        if a[j] == i:
                print(j, end=" ")
                p = True
if not p:
        print("Отсутствует")
