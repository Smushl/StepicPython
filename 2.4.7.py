s = input()
encoded = ""
i = 0
while i < len(s):
    c = s[i]
    encoded += c
    count =1
    for j in range(i+1, len(s)):
        if s[j] != c:
            break
        count += 1
        i += 1
    encoded += str(count)
    i +=1
print(encoded)

