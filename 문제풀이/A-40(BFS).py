"""
동빈이는 숨바꼭질을 하고 있는데, 1~N번 까지의 헛간 중에서
최단경로가 가장 먼 곳의 헛간이 가장 안전하다고 판단하고 있다.
동빈이가 생각하기에 어떤 헛간이, 얼마나 걸리며, 해당 헛간과 같은 
최단거리를 가지는 헛간의 갯수가 몇 개인지 생각해보려고 한다.
  (헛간은 M개의 길이가 1인 양방향 통로를 가진다.)
:첫 번째는 숨어야할 곳의 헛간의 번호 (최단길이가 같은 헛간이 여러개라면 가장작은 번호의 헛간을 출력)
:두 번째는 해당 헛간까지의 최단경로의 길이
:세 번째는 그 헛간과 같은 길이를 가지는 헛간의 갯수. 를 출력하여라
첫째줄에는 N,M이 다음과 같이 주어진다. (2<=N<=20,000, 1<=M<=50,000)
둘째줄부터 M+1줄까지 두 헛간 A,B 의 번호가 공백을 두고 주어진다. (1<=A,B<=N)
[Input]
6 7
3 6
4 3
3 2
1 3 
1 2
2 4
5 2
[output]
4 2 3
[풀이]
:1번헛간에서 2~N번까지의 헛간의 최단경로의 최대치를 구하는 문제.
  다익스트라로 distance를 구한 후 -> distance의 INF보다 작으면서 최대치를 구한다. 이때 INDEX와 COUNT를 한꺼번에 구한다.
    O(N)
"""
""" BFS 방식의 풀이 (distance값 추가해서 BFS 돌리기) """
# distacne[item] = distance[node] + 1 
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
def results(distance):
    maxs = index = count = 0
    for i in range(len(distance)):
        if maxs<distance[i]:
            maxs = distance[i]
            count = 1
            index = i 
        elif maxs == distance[i]:
            count += 1
    return index, maxs, count
    
def bfs(graph, visited):
    visited[1] = True
    distance = [0]*(len(visited))
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for item in graph[node]:
            if not visited[item]:
                visited[item] = True
                queue.append(item)
                distance[item] = distance[node] + 1 
    print(*results(distance))
bfs(graph, visited)
    
