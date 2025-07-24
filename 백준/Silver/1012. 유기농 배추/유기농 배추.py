from collections import deque

def bfs(sx,sy):
        queue = deque([(sx, sy)])
        cnt = 0
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        while queue:
             cx, cy = queue.popleft()
             for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if(0<=nx<m and 0<=ny<n):
                    if(f[nx][ny] == 1):
                        f[nx][ny] = 0
                        queue.append((nx,ny))

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    f= []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(0)
        f.append(row)

    for i in range(k):
        x, y = map(int, input().split())
        f[x][y] = 1
    
    cnt = 0

    for i in range(m):
        for j in range(n):
            if (f[i][j] == 1):
                bfs(i,j)
                cnt += 1
    
    print(cnt)