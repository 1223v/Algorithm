import sys
import heapq
input = sys.stdin.readline

V, M = map(int,input().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)


for _ in range(M):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))


J,S = map(int,input().split())
def dijkstra(start):
    hq = []
    distance = [float('inf')] *(V+1)
    distance[start] = 0
    visited[start] = True
    heapq.heappush(hq,(0, start))

    while hq:
        cost, now = heapq.heappop(hq)

        if distance[now] < cost:
            continue

        for next_node, dist in graph[now]:
            if distance[next_node] > cost + dist:
                distance[next_node] = cost + dist
                heapq.heappush(hq,(dist + cost, next_node))

    return distance

# J < S
J_distance = dijkstra(J)
S_distance = dijkstra(S)

total_distance = float('inf')
J_position = float('inf')
result = -1

# 순서 정렬
for i in range(1,V+1):
    if total_distance > J_distance[i] + S_distance[i] and i != J and i!= S:

        total_distance = J_distance[i] + S_distance[i]


for i in range(V,0,-1):
    if i != J and i != S and J_distance[i] < S_distance[i] and J_distance[i] + S_distance[i] == total_distance and J_distance[i] <= J_position:
        J_position = J_distance[i]
        result = i

print(result)