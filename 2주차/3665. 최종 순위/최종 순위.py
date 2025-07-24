from collections import deque

test = int(input())

for i in range(test):
    n = int(input())
    rank = list(map(int,input().split()))

    graph = []
    for j in range(n+1):
        arr = []
        graph.append(arr)
    in_Degree = [0]*(n+1)

    for i in range(n):
        for j in range(i+1,n):
            graph[rank[i]].append(rank[j])
            in_Degree[rank[j]] += 1
    m = int(input())
    for k in range(m):
        a, b = map(int,input().split())
        if(a in graph[b]):
            graph[b].remove(a)
            graph[a].append(b)
            in_Degree[b]+=1
            in_Degree[a]-=1
        elif(b in graph[a]):
            graph[a].remove(b)
            graph[b].append(a)
            in_Degree[a]+=1
            in_Degree[b]-=1
    
    def line():
        result = []
        queue = deque()
        for i in range(1, n +1):
            if(in_Degree[i] == 0):
                queue.append(i)
        
        while queue:
            if len(queue)>1:
                    return"?"
            cn = queue.popleft()
            result.append(cn)
            for nn in graph[cn]:
                in_Degree[nn] -= 1
                if(in_Degree[nn] == 0):
                    queue.append(nn)
        if len(result) != n:
            return "IMPOSSIBLE"
        return result
    
    answer = line()
    if(answer == "?" or answer == "IMPOSSIBLE"):
        print(answer)
    else:
        print(' '.join(map(str, answer)))
