with open('input.txt', 'r') as f:
    f = f.readlines()
    f = [[i[:int(len(i)/2)], i[int(len(i)/2):]] for i in f]

    errors = []
    for i in f:
        for j in i[0]:
            if j in i[1]:
                errors.append(j)
                break

    sum = 0
    for i in errors:
        i = ord(i)
        if i > 0b0110_0000:
            sum += i - 0b0110_0000
        else:
            sum += i - 0b0100_0000 + 26

        print(i, sum)
    print(errors, sum)