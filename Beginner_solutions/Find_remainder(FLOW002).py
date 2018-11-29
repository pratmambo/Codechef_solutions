n = int(input())
answer_list = []
for i in range(n):
    (a, b) = map(int, input().split())
    answer_list.append(a%b)

for i in answer_list:
    print(i)
