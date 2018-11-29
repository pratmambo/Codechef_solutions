n = int(input())

for i in range(n):
    routine = input()
    flag = True
    for j in range(len(routine)-1):
        if routine[j] > routine[j+1]:
            print("no")
            flag = False
            break
    if flag:
        print("yes")


