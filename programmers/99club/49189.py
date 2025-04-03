import heapq
from collections import defaultdict
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]

    for s,e in edge:
        graph[s].append((e,1))
        graph[e].append((s, 1))

    def dijkstra(start):
        hq = []
        distance = [float('inf')] * (n+1)

        heapq.heappush(hq,(0,start))
        distance[start] = 0

        while hq:
            dist, now_node = heapq.heappop(hq)

            for next_node, cost in graph[now_node]:
                if distance[next_node] > dist + cost:
                    distance[next_node] = dist + cost
                    heapq.heappush(hq,(dist+cost,next_node))

        return distance

    distance1 = dijkstra(1)

    max_result = defaultdict(int)

    for i in range(1,n+1):
        if float('inf') <= distance1[i]:
            continue

        max_result[distance1[i]] += 1


    return max_result[max(max_result.keys())]

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))