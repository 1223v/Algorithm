import sys
import heapq
input = sys.stdin.readline


N,M,X = map(int,input().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
distance1 = [float('inf')] * (N+1)
distance2 = [float('inf')] * (N+1)

for _ in range(M):
    s,e,cost = map(int,input().split())
    graph1[s].append((e,cost))
    graph2[e].append((s,cost))


def dijkstra(start):

    hq1 = []
    hq2 = []

    heapq.heappush(hq1,(0,start))
    heapq.heappush(hq2, (0, start))

    while hq1:
        dist, now_node = heapq.heappop(hq1)

        for next_node, cost in graph1[now_node]:
            if distance1[next_node] > cost + dist:
                distance1[next_node] = cost + dist
                heapq.heappush(hq1,(cost+dist, next_node))

    while hq2:
        dist, now_node = heapq.heappop(hq2)

        for next_node, cost in graph2[now_node]:
            if distance2[next_node] > cost + dist:
                distance2[next_node] = cost + dist
                heapq.heappush(hq2, (cost + dist, next_node))

    return distance1, distance2


dist1,dist2 = dijkstra(X)

max_value = 0
for i in range(1,N+1):
    max_value = max(max_value, dist1[i] + dist2[i])

print(max_value)
