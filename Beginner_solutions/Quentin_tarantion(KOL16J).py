for i in range(int(input())):
    length = int(input())
    flag = False
    chapters = list(map(int, input().split()))
    for j in range(1, length+1):
        if j in chapters:
            flag = True
        else:
            flag = False
            break
    if flag is True:
        for k in range(1, length+1):
            if chapters[k-1] == k:
                flag = False
            else:
                flag = True
                break
    if flag is True:
        print("yes")
    else:
        print("no")
