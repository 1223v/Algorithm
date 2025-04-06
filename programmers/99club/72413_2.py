import heapq
def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for _ in range(n+1)]

    for st,en,cost in fares:
        graph[st].append((en,cost))
        graph[en].append((st, cost))

    def dijkstra(start):
        hq = []
        distance = [float('inf')] * (n+1)

        heapq.heappush(hq,(0,start))
        distance[start] = 0

        while hq:
            dist, now_node = heapq.heappop(hq)

            if distance[now_node] < dist:
                continue

            for next_node, cost in graph[now_node]:
                if distance[next_node] > cost+dist:
                    distance[next_node] = cost+dist
                    heapq.heappush(hq,(cost+dist, next_node))

        return distance

    distance1 = dijkstra(s)
    max_value = distance1[a] + distance1[b]

    for i in range(n+1):
        if i == s:
            continue
        else:
            ab_distance = dijkstra(i)
            max_value = min(max_value, distance1[i]+ab_distance[a]+ab_distance[b])


    return max_value

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))



