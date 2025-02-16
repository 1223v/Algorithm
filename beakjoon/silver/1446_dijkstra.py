# https://www.acmicpc.net/problem/1446
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)

        if dist > distance[now]:
            continue

        for i in s[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq,(cost,i[0]))


N, D = map(int,input().split())
s = [[] for _ in range(D+1)]
distance = [int(1e9)] * (D+1)

for i in range(D):
    s[i].append((i+1,1))

for _ in range(N):
    start, end, l = map(int,input().split())
    if end > D:
        continue
    s[start].append((end,l))

dijkstra(0)
print(distance[D])