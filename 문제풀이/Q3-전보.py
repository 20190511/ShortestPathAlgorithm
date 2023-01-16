"""
첫째 줄에 도시의개수 N, 통로의 개수 M, 메시지를 보내야하는 도시 C 
둘째줄부터 M+1 번째 줄까지 특정도시(X) 에서 도착도시(Y) 까지 걸리는 통로의 길이 (Z) 가 주어집니다.
(1<=N<=30,000, 1<=M<=200,000, 1<=C<=N)
(1<X,Y<=N, 1<=Z<=1,000)

첫째 줄에 도시 C에서 보낼 수 있는 도시의 개수와 총 걸리는 시간을 출력하여라.


3 2 1 
1 2 4
1 3 2

[문제풀이]
다익스트라로 해결하면 되는데
해당 distance가 0(자기자신)이나 INF(못가는 노드)가 아닌 Node의 수를 Count로 하고,
distance의 최댓값이 정답이 된다.

[팁]
배열 안의 요소들을 그대로 출력하는 경우
list = [1,2,3,4,5,6,7,8]
print(*list)
로 해주면 1 2 3 4 5 6 7 8 과같이 출력된다. (literable 설정)

"""
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n,m,start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        lens, node = heapq.heappop(q)
        if lens > distance[node]:
            continue
        for item in graph[node]:
            cost = lens + item[1]
            if cost < distance[item[0]]:
                distance[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))

def counts(distance):
    count = 0
    times = -1
    for i in range(1, n+1):
        if 0<distance[i]<INF:
            count += 1
            if times < distance[i]:
                times = distance[i]
    return count, times
    
dijkstra(start)
print(*counts(distance))
