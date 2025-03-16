

import sys
input = sys.stdin.readline
import heapq

N, M, X = map(int,input().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,cost = map(int,input().split())
    graph1[s].append((e,cost))
    graph2[e].append((s,cost))

def dijkstra(start,graph):

    distance = [float('inf')] * (N+1)
    hq = []

    distance[start] = 0
    heapq.heappush(hq,(0, start))

    while hq:
        dist, now_node = heapq.heappop(hq)

        if distance[now_node] < dist:
            continue

        for next_node, cost in graph[now_node]:
            if distance[next_node] > dist + cost:
                distance[next_node] = dist + cost
                heapq.heappush(hq,(dist+cost, next_node))

    return distance

distance1 = dijkstra(X, graph1)
distance2 = dijkstra(X, graph2)

total_distance = 0
for i in range(1,N+1):
    tmp = distance1[i] + distance2[i]
    if tmp >= float('inf'):
        continue

    total_distance = max(tmp, total_distance)

print(total_distance)



