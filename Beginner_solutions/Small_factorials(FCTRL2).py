import math
n = eval(input())
factloist = []

for i in range(n):
    factloist.append(math.factorial(int(input())))

for i in factloist:
    print(i)
