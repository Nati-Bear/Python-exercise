import sys
from collections import deque
n = int(input())  #정사각형 칸 길이 입력
m = []        #지도 가로열 생성리스트
for i in range(n):
    r = list(map(int,input())) #전반적으로 지도 만드는 리스트, 입력받아서 값 저장
    m.append(r)

visited = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    visited.append(row)
answer = []
#bfs 탐색
def bfs(sx,sy):
    queue = deque([(sx, sy)])
    cnt = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if(0<=nx<n and 0<=ny<n):
                if ((m[nx][ny] == 1) and visited[nx][ny] == 0):
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if (m[i][j] == 1 and visited[i][j]==0):
            visited[i][j] = 1
            search = bfs(i,j)
            answer.append(search)

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i], end = "\n")
