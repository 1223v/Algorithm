# https://www.acmicpc.net/problem/1504

import sys
input = sys.stdin.readline
import heapq

N, M = map(int,input().split())


graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())

def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance = [float('inf')] * (N + 1)
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)

        if dist > distance[now]:
            continue

        for next_node, cost in graph[now]:
            if distance[next_node] > dist+cost:
                distance[next_node] = dist+cost
                heapq.heappush(hq, (dist+cost, next_node))

    return distance

distance_1 = dijkstra(1)
distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)

distance_v1_v2 = distance_1[v1] + distance_v1[v2] + distance_v2[N]
distance_v2_v1 = distance_1[v2] + distance_v2[v1] + distance_v1[N]

result = min(distance_v1_v2, distance_v2_v1)
if float('inf') <= result:
    print(-1)
else:
    print(result)
