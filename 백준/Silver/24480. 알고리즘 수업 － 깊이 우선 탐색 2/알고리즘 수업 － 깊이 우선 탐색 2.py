def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    line[t].reverse()
    for i in line[t]:
        if (visited[i] == 0):
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(10**6)  #재귀 깊이 확장
n, m ,r = map(int, sys.stdin.readline().split())
line = []  #노드를 저장하기 위한 리스트
for i in range(n+1):
    line.append([])
visited = [0]*(n+1)
cnt = 1
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    line[b].append(a)

dfs(r)
for i in range(1, n+1):
    print(visited[i])