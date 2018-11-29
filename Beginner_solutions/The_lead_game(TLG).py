n = int(input())
numlist = []
player = []
difference = []
player1_score, player2_score = 0, 0
for i in range(n):
    m = input().split()
    player1_score += int(m[0])
    player2_score += int(m[1])
    max_score = max(player1_score, player2_score)
    if max_score == player1_score:
        player.append(1)
        difference.append(player1_score - player2_score)
    else:
        player.append(2)
        difference.append(player2_score - player1_score)

maxdifference = max(difference)
index_player = difference.index(maxdifference)
playerans = player[index_player]

print(playerans, end=" ")
print(maxdifference)
