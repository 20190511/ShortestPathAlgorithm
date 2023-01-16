"""
길찾기 문제는 기본적으로 DP 구조를 따름.

그리디 알고리즘
매 생황에서 가장 비용이 작은 노드를 선택하는 방법

for 0 ... n: (LOOP):
 # j <- now -> (next, value)
 ## j[0]=b Node, j[1]=a->b Value
 distance[now] = min(j[1]+distance[now], distance[j[0]])



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
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input()) #시작 노드 입력받기.
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
  #a->b 가는데 비용c
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

#방문 X 노드 중 가장 작은 인덱스 O(N)
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  #시작노드 초기화
  for j in graph[start]:
    distance[j[0]] = j[1]

  for _ in range(n-1):
    now = get_smallest_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1] #start->a->b 과정.
      if cost < distance[j[0]]: #start->b 와 비교.
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
