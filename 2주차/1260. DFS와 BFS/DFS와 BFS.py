import sys
from collections import deque

sys.setrecursionlimit(10**6)  #재귀 깊이 확장

n, m ,r = map(int, sys.stdin.readline().split())
line = []  #노드를 저장하기 위한 리스트
for i in range(n+1):
    line.append([])

visited1 = [0]*(n+1)
visited2 = [0]*(n+1)

result1 = []
result2 = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    line[b].append(a)
for i in range(1, n+1):
    line[i].sort()

def dfs(t):
    visited1[t] = 1
    result1.append(t)
    for i in line[t]:
        if (visited1[i] == 0):
            dfs(i)

def bfs(t):
    visited2[t] = 1
    result2.append(t)
    queue = deque([t])#큐 생성
    while queue:
        current = queue.popleft()
        for i in line[current]:
            if (visited2[i] == 0):
                visited2[i] = 1
                queue.append(i)
                result2.append(i)

dfs(r)
print(' '.join(map(str, result1)))
bfs(r)
print(' '.join(map(str, result2)))
