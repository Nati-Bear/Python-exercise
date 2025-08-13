import sys
input = sys.stdin.readline
def solve():
    k = int(input())
    arr = list(map(int, input().split()))
    
    #dp 테이블 (i~j 합치는 최소비용 저장)
    dp = [[0]*k for _ in range(k)]
    
    #opt테이블(최적화용, dp[i][j]의 최적분할점 r
    opt = [[0]*k for _ in range(k)]
    
    #prefix sum : 리스트 앞에부터 차례대로 더한 값
    ps = [0]*(k+1)
    for i in range(k):
        ps[i+1] = ps[i] + arr[i]
        opt[i][i] = i
    
    for length in range(2,k+1):
        for i in range(k - length + 1):
            j = i + length - 1
            left = opt[i][j-1]
            right = opt[i+1][j]
            if right > j-1:
                right = j-1
            if left < i:
                left = i

            range_sum = ps[j+1]-ps[i]
            best_cost = float('inf')
            best_r = left
            for r in range(left,right+1):
                cost = dp[i][r] + dp[r+1][j] + range_sum
                if cost<best_cost:
                    best_cost = cost
                    best_r = r
            
            dp[i][j] = best_cost
            opt[i][j] = best_r
    
    return(dp[0][k-1])





t = int(input())
for _ in range(t):
    print(solve())