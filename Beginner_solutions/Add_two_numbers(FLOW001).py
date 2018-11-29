n = eval(input())
sumlist = []
for i in range(n):
    m = input().split()
    a = int(m[0])
    b = int(m[1])
    sumlist.append(a+b)

for i in sumlist:
    print(i)