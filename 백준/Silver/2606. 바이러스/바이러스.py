import sys
from collections import deque
com = int(sys.stdin.readline())
l = int(sys.stdin.readline())
list = []
for i in range(com+1):
    list.append([])
for i in range(l):
    a,b = map(int, sys.stdin.readline().split())
    list[a].append(b)
    list[b].append(a)
visited = [0]*(com+1)
virus = 0

def bfs(t):
    global virus
    queue= deque([t])
    visited[t] = 1
    while queue:
        current = queue.popleft()
        for i in list[current]:
            if(visited[i] == 0):
                queue.append(i)
                visited[i] = 1
                virus += 1

bfs(1)

print(virus)