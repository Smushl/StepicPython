# a = [i for i in input().split()]
# b =[]
# for s in a:
#     if s.lower() not in b:
#         b.append(s.lower())
# for s in b:
#     print(s, end=" ")
#     sum = 0
#     for s1 in a:
#         if s1.lower() == s.lower():
#             sum += 1
#     print(sum)

a = [i.lower() for i in input().split()]
for s in set(a):
    print(s, a.count(s))