import sys
input = sys.stdin.readline
import heapq

def dijkstra(graph, start):
    time = [int(1e9)] * (N+1)
    time[start] = 0

    hq = []
    heapq.heappush(hq, (0,start))
    while hq:
        c_time, c_com = heapq.heappop(hq)
        # if c_time < time[c_com]:
        #     continue
        for s, a in graph[c_com]:
            if c_time+s < time[a]:
                time[a] = c_time+s
                heapq.heappush(hq,(c_time+s, a))

    count, endTime = 0,0
    for t in time:
        if t < int(1e9):
            count += 1
            if t > endTime:
                endTime = t

    return count, endTime




TC = int(input())

for _ in range(TC):
    N, D, C = map(int,input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(D):
        a, b, s = map(int,input().split())
        graph[b].append((s,a))

    count, endTime = dijkstra(graph, C)
    print(count, endTime)