"""
첫 째줄에 T 케이스 T(1<=T<=10)가 주어진다
매 테스트 케이스마다 탐사크기를 의미하는 N 이 주어진다 (2<=N<=125)
이어서 N개의 줄에걸쳐 각 칸의 비용이 주어지며 공백으로 구분한다. (0<=각 칸의 비용<=9)

3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 4
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""
"""풀이 2 : 2차원 그래프 그대로 받기"""
# 2차원 그래프를 heapq.heappush(q, (graph[x][y], x,y)) 형태로 힙을 구성하고
# distance[x][y] 형태와 비교하면 된다. (1차원 노드를 2차원으로 볼 뿐인 문제)
import sys
import heapq
input = sys.stdin.readline
T = int(input())
INF = int(1e9)

def dijkstra(graph, n):
    x, y = 0, 0
    distance = [[INF]*n for _ in range(n)]
    distance[x][y] = graph[x][y]
    q = [(graph[x][y], x, y)]
    
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        lens, x, y = heapq.heappop(q)
        if lens > distance[x][y]:
            continue
        for dx,dy in dxdy:
            nx,ny = dx+x,dy+y
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            cost = graph[nx][ny] + lens
            if cost < distance[nx][ny]:
                heapq.heappush(q, (cost, nx, ny))
                distance[nx][ny] = cost
    return distance[n-1][n-1]
            
result = []
for _ in range(T):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    result.append(dijkstra(graph,n))
    

for item in result:
    print(item)





""" 원본 풀이 : 2차원 그래프 -> 1차원 그래프화"""
"""
import sys
import heapq
input = sys.stdin.readline
T = int(input())
INF = int(1e9)

def makeGraph(world, n):
    graph = [[] for _ in range(n*n+1)]
    count = 1 
    for a in range(n):
        for b in range(n):
            value = world[a][b]
            if a > 0:
                graph[count].append((count-n, value))
            if a < n-1:
                graph[count].append((count+n, value))
            if b > 0:
                graph[count].append((count-1, value))
            if b < n-1:
                graph[count].append((count+1, value))
            count += 1 
    return graph
    
def dijkstra(graph, n):
    q = []
    distance = [INF] * (n*n + 1)
    distance[1] = 0 #무조건 시작은 1`
    heapq.heappush(q, (0, 1))
    
    while q:
        lens, node = heapq.heappop(q)
        if lens > distance[node]:
            continue
        for item in graph[node]:
            cost = item[1] + lens
            if cost < distance[item[0]]:
                distance[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))
    return distance[-1]

result = []
for _ in range(T):
    n = int(input())
    world = []
    for _ in range(n):
        world.append(list(map(int, input().split())))
        
    graph = makeGraph(world, n) #O(NN)
    result.append(dijkstra(graph, n)+world[n-1][n-1]) #O(NlogN)

for item in result:
    print(item)
"""

