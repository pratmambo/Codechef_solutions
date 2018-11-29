n = int(input())

for i in range(n):
    val, div = 0, 2048
    num = int(input())
    while div != 0:
        val += num // div
        num %= div
        div = div // 2

    print(val)
