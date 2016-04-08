nukl = input()
sum = 0
nukl = nukl.upper()
for c in nukl:
    if c == 'C' or c == 'G':
        sum += 1
print(100 * sum / len(nukl))
