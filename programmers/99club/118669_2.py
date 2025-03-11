import heapq
def solution(n, paths, gates, summits):

    graph = [[] for _ in range(n+1)]
    summits_lst = [0] * (n+1)
    gates_lst = [0] * (n+1)

    for s,e,cost in paths:
        graph[s].append((e,cost))
        graph[e].append((s,cost))

    for i in summits:
        summits_lst[i] = 1

    for i in gates:
        gates_lst[i] = 1



    def dijkstra():
        top_node = 0
        intensity = float('inf')
        hq = []
        distance = [float('inf')] * (n+1)
        for i in gates:
            heapq.heappush(hq,(0,i))
            distance[i] = 0

        while hq:
            dist, now_node = heapq.heappop(hq)

            if dist > intensity:
                continue

            if summits_lst[now_node] == 1:
                if intensity > dist:
                    intensity = dist
                    top_node = now_node

            for next_node, cost in graph[now_node]:
                if distance[next_node] > max(cost,dist):
                    distance[next_node] = max(cost,dist)
                    heapq.heappush(hq,(max(cost,dist), next_node))

        return [top_node, intensity]


    return dijkstra()

print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],[5]))