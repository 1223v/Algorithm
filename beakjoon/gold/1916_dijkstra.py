import sys
import heapq
input= sys.stdin.readline

N = int(input())
M = int(input())
s = [[] for _ in range(N+1)]
distance = [float('inf')] * (N+1)

for _ in range(M):
    a, b, c = map(int,input().split())
    s[a].append((b,c))


start1,end1 = map(int,input().split())

min_value = int(1e9)
def dijkstra(start):
    global min_value

    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0

    while hq:
        cost, now = heapq.heappop(hq)

        if cost > distance[now]:
            continue

        for next, dist in s[now]:
            if distance[next] > cost + dist:
                distance[next] = cost + dist
                heapq.heappush(hq,(cost+dist, next))



dijkstra(start1)
print(distance[end1])