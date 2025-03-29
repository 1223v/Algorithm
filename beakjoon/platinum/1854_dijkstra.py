import sys
import heapq
input = sys.stdin.readline

N,M,K = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,cost = map(int,input().split())
    graph[s].append((e,cost))

def dijkstra(start):

    hq = []
    distance = [[] for _ in range(N+1)]

    heapq.heappush(hq,(0,start))
    heapq.heappush(distance[start],0)


    while hq:
        dist, now_node = heapq.heappop(hq)

        for next_node, cost in graph[now_node]:
            if len(distance[next_node]) < K:
                heapq.heappush(distance[next_node], -(cost + dist))
                heapq.heappush(hq,(cost+dist, next_node))

            elif -distance[next_node][0] > cost + dist:
                heapq.heappop(distance[next_node])
                heapq.heappush(distance[next_node], -(dist+cost))
                heapq.heappush(hq,(cost+dist,next_node))


    for i in range(1,N+1):
        if len(distance[i]) < K:
            print(-1)

        else:
            print(-distance[i][0])

dijkstra(1)
