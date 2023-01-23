#음수 간선의 순환을 감지할 수 있다 O(VE)
"""
[INPUT 1]
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2

[Output 1]
4
3

[INPUT 2]
3 4
1 2 4
1 3 3
2 3 -4
3 1 -2

[Output 2]
-1


[INPUT 3]
3 2
1 2 4
1 2 3

[Output 3]
3
-1
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0 
    for i in range(n):
        #모든 간선을 검사.
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]+dist[cur]
            #현재 간선이 INF라면 검사할 필요 없음.
            if dist[cur] != INF and dist[next_node]>cost:
                dist[next_node] = cost
                #n번째 Round에서도 값이 갱신된다면 음수 순환이 존재하는것.
                if i == n-1:
                    return True
    return False
    
n,m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
    
negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
            
