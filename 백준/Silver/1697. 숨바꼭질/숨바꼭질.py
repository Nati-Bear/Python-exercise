from collections import deque
n, k = map(int,input().split())

visited = [0]*100001
def bfs(t):
    queue = deque([t])
    while queue:
        cp = queue.popleft()
        if(cp == k):
            sec = visited[cp]
            return sec
        for i in (cp-1 , cp+1, cp*2):
            if(0<=i<100001 and visited[i] == 0):
                visited[i] = visited[cp]+1
                queue.append(i)                
result = bfs(n)
print(result)