import heapq
def solution(N, road, K):
    answer = []
    graph = [[] for _ in range(N+1)]
    for s,e,cost in road:
        graph[s].append((e,cost))
        graph[e].append((s, cost))


    def dijkstra(start):
        hq = []
        distance = [float('inf')] * (N+1)

        heapq.heappush(hq,(0,start))
        distance[start] = 0

        while hq:
            dist,now_node = heapq.heappop(hq)

            for next_node, cost in graph[now_node]:
                if distance[next_node] > cost + dist:
                    distance[next_node] = cost + dist
                    heapq.heappush(hq,(cost+dist, next_node))


        return distance


    distance1 =dijkstra(1)
    for i in range(1,N+1):
        if distance1[i] <= K:
            answer.append(i)

    return len(answer)

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))