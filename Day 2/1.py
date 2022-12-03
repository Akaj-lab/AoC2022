with open("input.txt", "r") as f:
    f = f.read()
    f = f.split("\n")

    f = [i.split(" ") for i in f]

    pay = {'X': 1, 'Y': 2, 'Z':3}

    opponent = {'A':'X', 'B':'Y', 'C':'Z'}

    score = 0
    for i, j in f:
        if (i == 'A' and j == 'X') or (i == 'B' and j == 'Y') or (i == 'C' and j == 'Z'):
            score += 3
        elif (i == 'A' and j == 'Y') or (i == 'B' and j == 'Z') or (i == 'C' and j == 'X'):
            score += 6
        score += pay[j]

    print(score)