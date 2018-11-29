for i in range(int(input())):
    length = int(input())
    list_numbers = list(map(int, input().split()))
    cost = list_numbers[0]
    for j in range(1, length):
        cost = cost | list_numbers[j]
    print(cost)
