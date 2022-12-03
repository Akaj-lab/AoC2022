with open('input.txt', 'r') as f:
    f = f.readlines()
    f = [f[i:i+3] for i in range(0, len(f), 3)]

    badges = []
    for i in f:
        for j in i[0]:
            if j in i[1] and j in i[2]:
                badges.append(j)
                break

    sum = 0
    for i in badges:
        i = ord(i)
        if i > 0b0110_0000:
            sum += i - 0b0110_0000
        else:
            sum += i - 0b0100_0000 + 26
    print(badges, sum)