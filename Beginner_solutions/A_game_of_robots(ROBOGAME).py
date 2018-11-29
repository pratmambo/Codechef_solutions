for i in range(int(input())):
    robots = input()
    movement_list = [0]*len(robots)
    position = 0
    flag = 0
    for j in robots:
        if j != ".":
            val = int(j)
            range_left = position - val
            if range_left < 0:
                range_left = 0
            range_right = position + val
            if range_right > (len(robots)-1):
                range_right = (len(robots)-1)
        else:
            range_right = -1
            range_left = 0
        for k in range(range_left, (range_right+1), 1):
            if movement_list[k] == 1:
                flag = 1
                print("unsafe")
                break
            else:
                movement_list[k] = 1
        position += 1
        if flag == 1:
            break
    if flag == 0:
        print("safe")
