"""
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

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] *(n+1)

#간선 입력받기
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))


def dijkstra(start):
  q = []
  #자기자신 간선길이, Node종류
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    offset, now = heapq.heappop(q)
    if distance[now] < offset:
      continue
      #item = (next, value(now->next))
    for item in graph[now]:
      cost = offset+item[1]
      if cost < distance[item[0]]:
        distance[item[0]] = cost
        heapq.heappush(q,(cost, item[0]))
dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("Infinity")
  else:
    print(distance[i])
  
