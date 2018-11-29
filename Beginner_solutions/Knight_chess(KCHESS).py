for i in range(int(input())):
    knight_list = []
    check = False
    free_to_move = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(int(input())):
        knight = list(map(int, input().split()))
        knight_list.append([knight[0],knight[1]])
    king_pos = list(map(int, input().split()))
    kingx = king_pos[0]
    kingy = king_pos[1]
    king_movement_list = [[kingx-1,kingy],[kingx,kingy-1],[kingx+1,kingy],[kingx,kingy+1],[kingx-1,kingy-1],[kingx-1,kingy+1],[kingx+1,kingy+1],[kingx+1,kingy-1]]
    for k in knight_list:
        if (abs(kingx-k[0]) == 2 and abs(kingy-k[1]) == 1) or (abs(kingx-k[0]) == 1 and abs(kingy-k[1]) == 2):
            check = True
        count = 0
        for postion in king_movement_list:
            if (abs(postion[0] - k[0]) == 2 and abs(postion[1] - k[1]) == 1) or (abs(postion[0] - k[0]) == 1 and abs(postion[1] - k[1]) == 2):
                free_to_move[count] = 1
            count += 1

    if sum(free_to_move) == 8 and check:
        print("YES")
    else:
        print("NO")