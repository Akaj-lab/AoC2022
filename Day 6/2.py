with open("input.txt", 'r') as f:
    f = f.readline()

    count = 14
    buffer = list(f[:14])
    true = True
    while true:
        buffer.pop(0)
        buffer.append(f[count])
        if len(set(buffer)) == 14:
            break
        count += 1
    print(count)