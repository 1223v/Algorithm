import heapq

def solution(n, paths, gates, summits):

    graph = [[] for _ in range(n+1)]
    is_gates = [False] *(n+1)
    is_summits = [False] * (n+1)
    distance = [float('inf')] * (n+1)

    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))

    for i in gates:
        is_gates[i] = True

    for i in summits:
        is_summits[i] = True

    def dijkstra():
        hq = []
        top_m = float('inf')
        intensity = float('inf')

        for i in gates:
            heapq.heappush(hq, (0, i))
            distance[i] = 0


        while hq:
            dist, now_node = heapq.heappop(hq)

            if dist > intensity:
                continue

            if is_summits[now_node]:
                if dist < intensity:
                    intensity = dist
                    top_m = now_node

                elif dist == intensity:
                    top_m = min(top_m, now_node)

                continue

            for next_node, cost in graph[now_node]:
                if not is_gates[next_node]:
                    if distance[next_node] > max(dist, cost):
                        distance[next_node] = max(dist, cost)
                        heapq.heappush(hq,(max(dist,cost), next_node))

        return [top_m, intensity]


    return dijkstra()


print(solution(7,
    [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
    [3, 7],
    [1, 5]
))
