with open("input.txt", 'r') as f:
    f = f.read().split()
    f = [[j.split("-") for j in i.split(",")] for i in f]

    g = []
    for i in f:
        if int(i[0][0]) <= int(i[1][0]):
            g.append(i)
        else:
            g.append(i[::-1])

    contains = 0
    for i in g:
        if int(i[0][1]) >= int(i[1][0]):
            contains += 1
        
    


    print(contains)
