n, m = map(int,input().split())

graph = []
for i in range(n+1):
    arr = []
    graph.append(arr)
in_Degree = [0]*(n+1)

for j in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    in_Degree[b] += 1

def line():
    queue = []
    result = []
    for i in range(1, n+1):
        if(in_Degree[i] == 0):
            queue.append(i)

    while queue:
        queue.sort()
        cn = queue.pop(0)
        result.append(cn)

        for nn in graph[cn]:
            in_Degree[nn] -= 1
            if(in_Degree[nn] == 0):
                queue.append(nn)
    return result

answer = line()
print(' '.join(map(str, answer)))