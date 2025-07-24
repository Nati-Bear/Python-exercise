import sys  #sys 호출
from collections import deque  #queue를 활용하기 위해 deque 호출
n, m ,r = map(int, sys.stdin.readline().split()) #n=정점의 수, #m=간선의 수, 시작 정점
line = []  #간선정보 저장용 리스트
for i in range(n+1) : 
    line.append([]) #line에 간선을 구성하는 정점을 담기위한 리스트 생성
visited = [0]*(n+1) #방문한 노드인지 파악, 무한루프에 빠지는거 방지
cnt = 1  #방문순서용, 최초에는 1
for i in range(m):  
    a, b = map(int, sys.stdin.readline().split()) #간선정보 저장
    line[a].append(b)  #해당 정점과 이어진 정점 저장
    line[b].append(a)  #양방향이므로 반대쪽에도 저장
for i in range(n+1):
    line[i].sort()
    line[i].reverse()

def bfs(t):
    global cnt  #cnt값이 변경되므로 이를 활용하기 위해 사용
    visited[t] = cnt #방문순서 저장
    queue = deque([t])#큐 생성
    while queue:
        current = queue.popleft()
        for i in line[current]:
            if (visited[i] == 0):
                cnt +=1
                queue.append(i)
                visited[i] = cnt

bfs(r)

for i in range(1, n+1):
    print(visited[i])