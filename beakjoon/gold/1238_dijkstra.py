import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    A,B,T = map(int,input().split())
    graph[A].append((B,T))

def dijkstra(start):
    distance = [float('inf')] * (N + 1)
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)

        if dist > distance[now]:
            continue

        for next_node, cost in graph[now]:
            if distance[next_node] > dist + cost:
                distance[next_node] = dist + cost
                heapq.heappush(hq,(dist+cost, next_node))

    if start == X:
        return distance
    return distance[X]

result = [0] * (N+1)
for i in range(1,N+1):
    if X != i:
        result[i] = dijkstra(i)

    else:
        tmp2 = dijkstra(i)

for i in range(1,N+1):
    result[i] += tmp2[i]


print(max(result))