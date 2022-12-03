with open("input.txt", "r") as f:
    f = f.read()
    f = f.split("\n\n")

    l = []

    for i in f:
        l.append(list(map(int, i.split("\n"))))

    sum = []
    for i in l:
        s = 0
        for j in i:
            s += j
        sum.append(s)
    sum.sort()
    print(sum)