"""
Q2. 미래도시
첫째 줄에 전체 회사의 개수 N 과 경로의 개수 M 이 공백으록 구분되어 입력된다.
둘째줄부터 M+1 줄 까지 연결된 두 회사의 번호가 공백으로 구분되어 주어진다. (두 회사의 거리는 1 (time)이다.)
M+2 번째 줄에는 X(최종 목적지 회사), K(경유해야하는 회사) 가 주어진다.
시작은 1번 회사로 한다.

만약 K=3, X=2라면, 1번회사->3번회사->2번회사 로 가는 최소시간을 구하여라.
(1<= N,M <=100)
(1<= K <=100)


<Input>
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5


4 2
1 3
2 4
3 4

<output>
3

-1

[풀이]
전형적인 플로이드 워샬(Floyd-Warshall) 알고리즘이다.
원래는 삼각형 형태의 graph 로 구현해도 되만 구현 난이도를 줄이기 위해
입력을 받을 때,
graph[a][b] = graph[b][a] = 1 
로 두고 플로이드 워샬 알고리즘으로 해결하면 쉽다
시간 복잡도는 O(NNN) 이 될 것이다.
"""

import sys
INF = int(1e9)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0 
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 
final,mid = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

count = graph[1][mid] + graph[mid][final]
if 0<count<INF:
    print(count)
else:
    print(-1)

