import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
S = int(input())
graph = [[] for _ in range(V+1)]
distance = [float('inf')] * (V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    #graph[v].append((u, w))

def dijkstra():
    hq = []
    heapq.heappush(hq, (0,S))
    distance[S] = 0

    while hq:
        dist, now = heapq.heappop(hq)

        if dist > distance[now]:
           continue

        for next_node, cost in graph[now]:
            if distance[next_node] > dist + cost:
                distance[next_node] = dist + cost
                heapq.heappush(hq,(dist + cost, next_node))


dijkstra()

for i in range(1,V+1):
    if float('inf') != distance[i]:
        print(distance[i])
    else:
        print("INF")

