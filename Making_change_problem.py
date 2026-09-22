coins = [1, 2, 5]
amount = 5

n = len(coins)
m = amount + 1
dp = [[0] * m for _ in range(n)]
for j in range(m):
    if j % coins[0] == 0:
        dp[0][j] = 1
for i in range(1, n):
    for j in range(m):

        dp[i][j] = dp[i - 1][j]

        if j >= coins[i]:
            dp[i][j] += dp[i][j - coins[i]]

for row in dp:
    print(row)

print("Number of combinations =", dp[n - 1][amount])
