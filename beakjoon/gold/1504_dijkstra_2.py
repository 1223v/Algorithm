import sys
input = sys.stdin.readline
import heapq

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    s,e,cost = map(int,input().split())
    graph[s].append((e,cost))
    graph[e].append((s,cost))

p1,p2 = map(int,input().split())

def dijkstra(start, end):

    hq = []
    distance = [float('inf')] * (N+1)

    distance[start] = 0
    heapq.heappush(hq,(0,start))

    while hq:
        cost, now = heapq.heappop(hq)

        if distance[now] < cost:
            continue

        for next_node, dist in graph[now]:
            if distance[next_node] > dist + cost:
                distance[next_node] = dist + cost
                heapq.heappush(hq,(dist+cost, next_node))


    return distance[end]

x1 = dijkstra(1,p1)
y1= dijkstra(p1,p2)
z1 = dijkstra(p2,N)

x2 = dijkstra(1,p2)
y2= dijkstra(p2,p1)
z2 = dijkstra(p1,N)

result =min(x1+y1+z1, x2+y2+z2)

if result < float('inf'):
    print(result)
else:
    print(-1)
