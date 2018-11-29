for i in range(int(input())):
    l = []
    total = 0
    for j in range(int(input())):
        a = input()
        s = 2
        for k in range(1, len(a)):
            if a[k] == 'd' or a[k] == 'f':
                if a[k - 1] == 'd' or a[k - 1] == 'f':
                    s += 4
                else:
                    s += 2
            else:
                if a[k - 1] == 'j' or a[k - 1] == 'k':
                    s += 4
                else:
                    s += 2

        if a in l:
            total += int(s / 2)
        else:
            total += s
            l.append(a)

    print(total)
