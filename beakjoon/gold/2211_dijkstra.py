import sys
input = sys.stdin.readline
import heapq

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
distance = [float('inf')] * (N+1)
parent = [0]*(N+1)
for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

def dijkstra(start):

    hq = []
    distance[start] = 0
    heapq.heappush(hq,(0,start))

    while hq:
        cost, now = heapq.heappop(hq)

        if distance[now] < cost:
            continue

        for next, dist in graph[now]:

            if distance[next] > cost+dist:
                parent[next] = now

                distance[next] = cost+dist
                heapq.heappush(hq,(cost+dist, next))


dijkstra(1)

count = 0
for i in distance:
    if i != 0 and i != float('inf'):
        count += 1

print(count)
for i in range(2, N + 1):
    print(parent[i],i)
