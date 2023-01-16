"""
경로 출력 다익스트라
아이디어 :
  다익스트라 cost를 갱신할 때, 해당 노드의 값을 path에 넣고 path를 반복호출하여 0이나올떄까지 역출력한다.
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2 
"""


import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
size, n = map(int, input().split())
start = int(input())
distance = [INF] * (size+1)
latest_path = [0] * (size+1)
graph = [[] for _ in range(size+1)]

for _ in range(n):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    distance[start] = 0 
    q = []
    heapq.heappush(q, (0,start))
    
    while q:
        length, node = heapq.heappop(q)
        if length > distance[node]:
            continue
        for item in graph[node]:
            cost = length + item[1]
            if cost < distance[item[0]]:
                distance[item[0]] = cost
                latest_path[item[0]] = node
                heapq.heappush(q, (cost, item[0]))

def navigate(path):
    navi = [[] for i in range(size+1)]
    strs = [""] * (size+1)
    for i in range(1, size+1):
        next = path[i]
        if not 0<next<INF:
            continue
        while 0<next<INF:
            navi[i].append(str(next))
            next = path[next]
        navi[i].reverse()
        if len(navi[i]) != 0:
            strs[i] = "->".join(navi[i])+"->"+str(i)
        else:
            strs[i] = str(i)
    return strs


dijkstra(start)
navi = navigate(latest_path)
for x in range(1, size+1):
    if distance[x] == INF:
        print("Infinity")
    else:
        print(distance[x],navi[x])
