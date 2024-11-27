import sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())

s = [[] for _ in range(N+1)]
dis = [sys.maxsize] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0

    while q:
        post_cost, now = heapq.heappop(q)
        if dis[now] < post_cost:
            continue

        for ab,c in s[now]:
            cost = post_cost + c
            if cost < dis[ab]:
                dis[ab] = cost
                heapq.heappush(q,(cost, ab))


for _ in range(M):
    a,b,c = map(int,input().split())

    s[a].append((b,c))
    s[b].append((a,c))

dijkstra(1)
print(dis[N])