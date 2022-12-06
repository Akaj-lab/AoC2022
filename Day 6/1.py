with open("input.txt", 'r') as f:
    f = f.readline()

    count = 4
    buffer = list(f[:4])
    true = True
    while true:
        buffer.pop(0)
        buffer.append(f[count])
        if len(set(buffer)) == 4:
            break
        count += 1
    print(count)