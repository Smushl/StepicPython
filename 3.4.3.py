with open("C:\\1.txt") as f:
    b = [i.lower() for i in f.read().split()]
    max = b[0]
    for c in set(b):
        if (b.count(c) > b.count(max)) or (b.count(c) == b.count(max)) and (c < max):
            max = c
    print(max, b.count(max))