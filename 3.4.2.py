def unzip(s):
    result = ""
    for i in range(len(s)):
        if s[i] not in "0123456789":
            cif = ""
            j = i + 1
            while  (j <= len(s)-1) and (s[j] in "0123456789"):
                    cif += s[j]
                    j +=1
            result += s[i]*int(cif)

    return result

s = input()
print(unzip(s))