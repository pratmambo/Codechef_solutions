inputs = input().split()
n = int(inputs[0])
k = int(inputs[1])
count = 0
for i in range(n):
    if int(input()) % k == 0:
        count += 1

print(count)

