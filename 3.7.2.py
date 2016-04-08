s1, s2, code, decode, coded, decoded = input(), input(), input(), input(), ' ', ' '
for c in code: coded += s2[s1.find(c)]
print(coded)
for c in decode: decoded += s1[s2.find(c)]
print(decoded)
