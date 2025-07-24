from collections import deque
t = int(input())
for i in range(t):
    l = int(input())
    board = []
    for j in range(l):
        row = [0]*l
        board.append(row)
    fx, fy  = map(int, input().split())
    ex, ey = map(int, input().split())
    ep = board[ex-1][ey-1]
    
    def bfs(sy,sx):
        queue =deque([(sy,sx)])
        dy = [-2,-1,1,2,2,1,-1,-2]
        dx = [1,2,2,1,-1,-2,-2,-1]
        while queue:
            cy,cx = queue.popleft()
            if(cy == ey and cx == ex):
                return board[cy][cx]
            for i in range(8):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if(0<=ny<l and 0<=nx<l):
                    if(board[ny][nx] == 0):
                        board[ny][nx] = board[cy][cx] + 1
                        queue.append((ny, nx))
    result = bfs(fy, fx)
    print(result)
