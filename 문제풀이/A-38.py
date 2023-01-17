"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
문제 리뷰 : n명의 학생이 있을 때, 
1번학생의 성적 < 5번의 학생의 성적
3번학생의 성적 < 4번의 학생의 성적
4번학생의 성적 < 2번의 학생의 성적
4번학생의 성적 < 6번의 학생의 성적
5번학생의 성적 < 2번의 학생의 성적
5번학생의 성적 < 4번의 학생의 성적
이렇게 6가지의 성적 비교만을 가지고 있다.
특정 학생의 정확한 순위를 알고자 할 때,
4번학생의 경우에는 4번학생보다 성적이 높은사람 2명, 낮은사람 3명으로 3등임을 명확히 알 수 있다.
하지만, 3번 학생의 경우에는, 5번학생과 1번학생과의 순위가 겹쳐 정확하게 알 수 없다.

이때, 정확하게 성적 순위를 알 수 있는 사람은 몇 명인가?
첫 째 줄에는 학생들의 수 N, 성적을 비교한 횟수 M 이 주어진다. (2<=N<=500, 2<=M<=50,000)
둘 째줄부터 M+1번째 줄까지는 성적을 비교한 결과인 A,B가 주어진다. (이는 A학생이 B학생보다 성적이 낮음을 의미한다.)



문제풀이 : 
    입력받을 때, 성적이 낮은 학생만 입력받는 단방향 그래프를 그린다. 
        (혹은 높은 학생만 입력받는 단방향 그래프.)
    이를 이용하여 플로이드-워샬 알고리즘으로 graph를 최신화한다.
    graph[a][b] 와 graph[b][a] 중 어느하나라도 갈 수 있는 경로가 존재한다면, 
        해당 a<->b 간의 순위를 표현할 수 있음을 의미한다.
    그렇게 n번째 노드가 n개의 노드(자신포함)가 모두 도달할 수 있는 그래프라면 
        정확한 순위가 알 수 있는 노드가 된다.
    
"""

import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1 
    
for a in range(1, n+1):
    for b in range (1, n+1):
        if a==b:
            graph[a][b] = 0 

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
for a in range(1, n+1):
    count = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            print(a,"->",b,"=",graph[a][b],sep="")
            count += 1 
    if count == n:
        result += 1 

print(result)
