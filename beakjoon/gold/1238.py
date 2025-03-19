import sys
import heapq
input = sys.stdin.readline


N,M,X = map(int,input().split())
graph1 = [[] for _ in range(N+1)]




for _ in range(M):
    s,e,cost = map(int,input().split())
    graph1[s].append((e,cost))



def dijkstra1(start):

    hq1 = []
    distance1 = [float('inf')] * (N + 1)

    heapq.heappush(hq1,(0,start))


    while hq1:
        dist, now_node = heapq.heappop(hq1)

        for next_node, cost in graph1[now_node]:
            if distance1[next_node] > cost + dist:
                distance1[next_node] = cost + dist
                heapq.heappush(hq1,(cost+dist, next_node))


    return distance1[X]


def dijkstra2(start):
    hq1 = []
    distance1 = [float('inf')] * (N + 1)

    heapq.heappush(hq1, (0, start))

    while hq1:
        dist, now_node = heapq.heappop(hq1)

        for next_node, cost in graph1[now_node]:
            if distance1[next_node] > cost + dist:
                distance1[next_node] = cost + dist
                heapq.heappush(hq1, (cost + dist, next_node))

    return distance1

result = [0] * (N+1)
dist1 = []
for i in range(1,N+1):
    if i != X:
        result[i] = dijkstra1(i)

    else:
        dist1 = dijkstra2(i)



max_value = 0
for i in range(1,N+1):
    max_value = max(max_value, result[i] + dist1[i])

print(max_value)
