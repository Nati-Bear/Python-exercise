import sys
input = sys.stdin.readline

n = int(input())   #추 갯수
chu = list(map(int, input().split()))  #추 무게 리스트
m = int(input()) #구슬 개수
bead = list(map(int, input().split())) #구슬 무게 리스트

maxw = 40000  #추로 만들수 있는 최대 무게 차이

dp = [False]*(maxw+1)
dp[0] = True
for i in chu:
    possible = []
    for w in range(len(dp)):
        if dp[w]:
            if (w+i) <= maxw:
                possible.append(w+i)
            possible.append(abs(w-i))
    for j in possible:
        dp[j] = True
    
result = []

for b in bead:
    if b > maxw:
        result.append('N')
    elif dp[b]:
        result.append('Y')
    else:
        result.append('N')

print(' '.join(result))