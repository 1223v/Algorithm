#  건물 짓는 순서가 정해져 있지 않음
# 1번 건물 건설 후 2, 3번이 가능  -> 4번이 가능
# 특정 건물을 가장 빨리 지을때까지 걸리는 최소시간 프로그램

# N = 건물의 갯수
# K = 건설 순서 규칙의 총 개수

# D1,D2, D3 ... => 건물 당 걸리는 시간
# 건설 순서 x,y (x -> y)

# W = 건설해야할 건물 번호

import sys
input = sys.stdin.readline
from collections import deque

TC = int(input())

def bfs(graph, indegree):
    queue = deque()


    for i in range(1,len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = D[i]

    while queue:
        node = queue.popleft()

        if node == W:
            print(dp[W])
            break

        for i in graph[node]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[node] + D[i])
            if indegree[i] == 0:

                queue.append(i)



for _ in range(TC):
    N, K = map(int,input().split())

    D = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    degree = [float('inf')] + [0] * (N)

    for _ in range(K):
        s, e = map(int,input().split())
        graph[s].append(e)
        degree[e] += 1

    W = int(input())

    dp = [0] * (N+1)


    bfs(graph, degree)
