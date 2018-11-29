for i in range(int(input())):
    (n, k) = map(int, input().split())
    score_list = list(map(int,input().split()))
    score_list = sorted(score_list, reverse=True)
    ans = k
    while True:
        if ans <= n-1 and score_list[ans-1] == score_list[ans]:
            ans += 1
        else:
            break
    print(ans)
