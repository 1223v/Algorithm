import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [[int(1e9)] * (K + 1) for _ in range(N+1)]

for _ in range(M):
    start, end, distance = map(int,input().split())
    graph[start].append((end,distance))
    graph[end].append((start, distance))

def dijkstra():
    hq = []
    heapq.heappush(hq, (0,1,K))
    visited[1][K] = 0

    while hq:
        dist, now, dp_k = heapq.heappop(hq)
        if dist > visited[now][dp_k]:
            continue

        for next_node,cost in graph[now]:

            # K 사용 안함으로 인해 비용 추가
            if visited[next_node][dp_k] > dist+cost:
                visited[next_node][dp_k] = dist+cost
                heapq.heappush(hq, (dist+cost,next_node,dp_k))

            # K 사용으로 인해 비용 제거
            if dp_k> 0 and visited[next_node][dp_k-1] > dist:
                visited[next_node][dp_k-1] = dist
                heapq.heappush(hq, (dist, next_node, dp_k-1))

dijkstra()
print(min(visited[N]))