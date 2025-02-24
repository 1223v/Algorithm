import heapq
def solution(n, s, a, b, fares):
    answer = 0
    graph=[[] for _ in range(n+1)]
    for start, end, cost in fares:
        graph[start].append((end,cost))
        graph[end].append((start, cost))

    def dijkstra(start):
        hq = []
        distance = [float('inf')] * (n+1)

        distance[start] = 0
        heapq.heappush(hq,(0,start))

        while hq:
            dist, now_node = heapq.heappop(hq)

            for next_node, cost in graph[now_node]:
                if distance[next_node] > dist+cost:
                    distance[next_node] = dist + cost
                    heapq.heappush(hq,(dist+cost, next_node))

        return distance

    origin_distance = dijkstra(s)
    result = origin_distance[a] + origin_distance[b]

    for i in range(n+1):
        if i == s:
            continue
        else:
            ab_distance=dijkstra(i)
            result = min(result, origin_distance[i] + ab_distance[a] + ab_distance[b])

    return result


print(solution(6,4,6,2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))