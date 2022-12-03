with open("input.txt", "r") as f:
    f = f.read()
    f = f.split("\n")

    f = [i.split(" ") for i in f]

    pay = {'X': 0, 'Y': 3, 'Z':6}

    score = 0
    for i, j in f:
        if j == "X":
            if i == 'A':
                score += 3
            elif i == 'B':
                score += 1
            elif i == 'C':
                score += 2
        
        elif j == 'Y':
            if i == 'A':
                score += 1
            elif i == 'B':
                score += 2
            elif i == 'C':
                score += 3

        elif j == 'Z':
            if i == 'A':
                score += 2
            elif i == 'B':
                score += 3
            elif i == 'C':
                score += 1

        score += pay[j]

    print(score)