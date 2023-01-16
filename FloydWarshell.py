# 각 단게마다 특정한 노드 k를 거쳐가는 경우의수를 확인하는 기법
"""
O(N*N*N) : 다익스트라 보다 비효율적일 수 있다.
# 각 단계에서 특정노드 k를 거쳐간 값이 크냐, 한번에 가는 값이 크냐 비교
Dab = min(Dab, Dak+Dkb)

0단계 : 각 노드에서 각 노드로 가는 비용으로 모두 초기화.
#자기 자신을 제외한 경유 거리로 비교한다.
1단계 : 1번노드를 거쳐가는 경우의 수를 고려하여 테이블 갱신 Dab = min(Dab, Da1+D1b)
2단계 : 2번노드를 거쳐가는 경우의 수를 고려하여 테이블 갱신 Dab = min(Dab, Da2+D2b)
...
n단계 : n번노드를 거쳐가는 경우의 수를 고려하여 테이블 갱신 Dab = min(Dab, Dan+Dnb)


4
7
1 2 4
1 4 6
2 1 3 
2 3 7
3 1 5
3 4 4
4 3 2
"""
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]



#자기 자신은 0으로
for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b] = 0

for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a][b] = c


for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print("Infinity", end=" ")
    else:
      print(graph[a][b], end=" ")
  print()
