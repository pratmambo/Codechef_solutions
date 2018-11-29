def sumcalc(nu):
    sumnu = 0
    while nu > 0:
        m = nu % 10
        sumnu += m
        nu = nu // 10
    return sumnu


n = int(input())
sumlist = []
for i in range(n):
    sumlist.append(sumcalc(int(input())))

for i in sumlist:
    print(i)