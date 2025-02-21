import sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())
distance = [[float('inf')] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
result = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s,e,cost = map(int,input().split())
    graph[s].append((e,cost))
    graph[e].append((s,cost))
    result[s][e] = e
    result[e][s] = s

def dijkstra(start):
    hq = []
    distance[start][start] = 0

    heapq.heappush(hq,(0,start))

    while hq:
        dist, now_node = heapq.heappop(hq)
        if distance[start][now_node] > dist:
            continue
        for next_node, cost in graph[now_node]:
            if distance[start][next_node] > dist + cost:
                distance[start][next_node] = dist + cost
                if now_node == start:
                    result[start][next_node] = next_node
                else:
                    result[start][next_node] = result[start][now_node]
                heapq.heappush(hq,(dist+cost, next_node))


for i in range(1,N+1):
    dijkstra(i)

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            print('-',end=' ')
        else:
            print(result[i][j], end= ' ')
    print()
