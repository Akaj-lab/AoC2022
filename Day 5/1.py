with open("input.txt", 'r') as f:
    f = f.read()

    input = f.split("\n\n")[1].split("\n")

    stack = [
        ['B', 'Z', 'T'],
        ['V', 'H', 'T', 'D', 'N'],
        ['B', 'F', 'M', 'D'],
        ['T', 'J', 'G', 'W', 'V', 'Q', 'L'],
        ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'],
        ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'],
        ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'],
        ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'],
        ['M', 'Q', 'L', 'F', 'D', 'S']
    ]
    
    for i in input:
        tmp = i.split(" ")
        am = int(tmp[1])
        fr = int(tmp[3]) - 1
        to = int(tmp[5]) - 1
        for _ in range(am):
            stack[to].append(stack[fr].pop())
    
    print(stack)