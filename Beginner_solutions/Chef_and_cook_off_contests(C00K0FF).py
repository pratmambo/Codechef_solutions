for i in range(int(input())):
    length = int(input())
    pd = []
    for j in range(length):
        pd.append(input())
    if pd.count("cakewalk") >= 1 and pd.count("simple") >= 1 and pd.count("easy") >= 1 and(pd.count("easy-medium") or pd.count("medium") >= 1) and(pd.count("medium-hard") or pd.count("hard") >= 1):
        print("Yes")
    else:
        print("No")
