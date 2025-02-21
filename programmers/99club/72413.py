import heapq
def solution(n, s, a, b, fares):
    answer = 0
    distance = [(float('inf'))] * (n+1)
    graph = [[] for _ in range(n+1)]
    result = [[] for _ in range(n+1)]

    for start, end, cost in fares:
        graph[start].append((end,cost))
        graph[end].append((start,cost))



    def dijkstra(start):
        hq =[]
        distance[start] = 0
        heapq.heappush(hq,(0, start))

        while hq:
            dist, now_node = heapq.heappop(hq)

            if distance[now_node] > dist:
                continue

            for next_node, cost in graph[now_node]:
                if distance[next_node] > cost + dist:
                    result[next_node].append((now_node,cost))
                    distance[next_node] = cost + dist
                    heapq.heappush(hq,(dist+cost, next_node))

        print(result)
        print(distance)

        res = set()
        ak = a
        bk = b

        while ak != start and bk != start:


            res.add(result[ak][0])
            res.add(result[bk][0])
            ak = result[ak][0][0]
            bk = result[bk][0][0]

        total = 0
        res_lst = list(res)
        print(res_lst)
        for i in range(len(res_lst)):
            total += res_lst[i][1]

        return total



    return dijkstra(s)

print(solution(6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))