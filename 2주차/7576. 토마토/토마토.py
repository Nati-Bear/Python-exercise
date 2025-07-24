from collections import deque
m, n = map(int,input().split())
box = []
for i in range(n):
    row = list(map(int, input().split()))
    box.append(row)

def bfs():
    queue = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                    queue.append((i,j))
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if(0<=nx<n and 0<=ny<m):
                if (box[nx][ny] == 0):
                    box[nx][ny] = box[cx][cy]+1
                    queue.append((nx,ny))
    
bfs()

day = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
        else : day = max(day, box[i][j]) #day와 box[i][j] 비교하여 큰 값을 day에 저장
        
print(day-1)
