with open("Day 10/input.txt", 'r') as f:
    f = f.readlines()
    a = []
    for i in f:
        a.append("noop")
        if i[0:3] == 'add':
            a.append(i[:-1])

    X = 1
    state = [1]
    for i in range(len(a)):
        z = a[i]
        if z[0:3] == 'add':
            X += int(z.split(" ")[1])
        state.append(X)

    ugh = ["", "", "", "", "", ""]
    for j in range(6):
        for i in range(40):
            st = state[i + j*40]
            if st - 1 == i or st == i or st + 1 == i:
                ugh[j] += '#'
            else:
                ugh[j] += '.'

    for i in range(6): print(ugh[i])