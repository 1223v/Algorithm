import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,cost = map(int,input().split())
    graph[s].append((e,cost))

start, end = map(int,input().split())

def dijkstra(start,end):

    hq = []
    distance = [float('inf')] * (N+1)

    heapq.heappush(hq,(0,start))
    distance[start] = 0

    city = [i for i in range(N+1)]

    while hq:

        dist, now_node = heapq.heappop(hq)

        if distance[now_node] < dist:
            continue

        for next_node, cost in graph[now_node]:
            if distance[next_node] > cost + dist:
                distance[next_node] = cost + dist
                heapq.heappush(hq,(cost + dist, next_node))
                city[next_node] = now_node

    print(distance[end])
    # print(distance)

    result = [end]
    while city[end] != end:
        result.append(city[end])
        end=city[end]

    print(len(result))
    print(*result[::-1])

dijkstra(start,end)



