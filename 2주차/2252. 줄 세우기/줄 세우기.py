from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n+1):
    arr = []
    graph.append(arr)

inDegree = [0]*(n+1)

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    inDegree[b] += 1

def line():
    result = []
    queue = deque()
    for i in range(1, n+1): #노드(학생번호)가 1부터 시작
        if(inDegree[i] == 0):
            queue.append(i)

    while queue:
        cn = queue.popleft()
        result.append(cn)

        for nn in graph[cn]:
            inDegree[nn] -= 1
            if(inDegree[nn] == 0):
                queue.append(nn)
    
    return result

answer = line()
print(' '.join(map(str, answer)))
