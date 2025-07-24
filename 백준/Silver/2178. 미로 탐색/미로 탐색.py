from collections import deque
n, m = map(int,input().split())  #정사각형 칸 길이 입력
maze = []        #지도 가로열 생성리스트
for i in range(n):
    r = list(map(int,input())) #전반적으로 지도 만드는 리스트, 입력받아서 값 저장
    maze.append(r)

#bfs 탐색
def bfs(sx,sy):
    queue = deque([(sx, sy)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if(0<=nx<n and 0<=ny<m):
                if (maze[nx][ny] == 1):
                    maze[nx][ny] = maze[cx][cy]+1
                    queue.append((nx,ny))

    return maze[n-1][m-1]

result = bfs(0,0)
print(result)