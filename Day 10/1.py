with open("Day 10/input.txt", 'r') as f:
    f = f.readlines()
    a = []
    for i in f:
        a.append("noop")
        if i[0:3] == 'add':
            a.append(i[:-1])

    X = 1
    state = []
    for i in range(len(a)):
        z = a[i]
        if z[0:3] == 'add':
            X += int(z.split(" ")[1])
        state.append(X)

    print(state[18]*20 + state[58]*60 +state[98]*100 +state[138]*140 +state[178]*180 +state[218]*220)