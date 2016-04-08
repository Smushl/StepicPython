with open("C:\\dataset_3363_4.txt") as f:
    mat = 0
    fiz = 0
    rus = 0
    lines = 0
    for line in f:
        line = line.strip()
        lines += 1
        # print(line)
        list = [i for i in line.split(";")]
        avg = (float(list[1]) + float(list[2]) +float(list[3]))/3
        mat += float(list[1])
        fiz += float(list[2])
        rus += float(list[3])
        print(avg)
        # print(list[0], )
    print(mat/lines, fiz/lines, rus/lines)
