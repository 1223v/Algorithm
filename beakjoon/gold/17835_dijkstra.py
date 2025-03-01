import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    s,e,cost = map(int,input().split())
    graph[e].append((s,cost))

K_lst = list(map(int,input().split()))


def dijkstra():

    hq = []
    distance = [float('inf')] * (N + 1)

    for start in K_lst:
        heapq.heappush(hq,(0,start))
        distance[start] = 0


    while hq:
        dist, now_node = heapq.heappop(hq)

        if distance[now_node] < dist:
            continue

        for next_node, cost in graph[now_node]:
            if distance[next_node] > dist + cost:
                distance[next_node] = dist + cost
                heapq.heappush(hq,(dist+cost, next_node))







# 면접장까지 가장 거리가 먼 도시 번호 출력
# 면접장까지 가장 거리가 먼 도시의 길이 출력
max_value, max_point = 0,0
dijkstra()

for i,m in enumerate(distance):


    if max_point != i and max_value < m:
        max_value, max_point = m, i

    elif max_point == i and max_value > m:
        max_value = m



print(max_point)
print(max_value)
