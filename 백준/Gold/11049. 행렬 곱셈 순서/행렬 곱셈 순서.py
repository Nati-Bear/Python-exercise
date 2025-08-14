import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    r, c = map(int,input().split())
    arr.append((r,c))
dp = [[0]*n for _ in range(n)]


for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length -1
        dp[i][j] = 2**31

        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])