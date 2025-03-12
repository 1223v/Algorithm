import sys
import heapq
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N,M,T = map(int,input().split())
    S,G,H = map(int,input().split())

    t_lst = []
    graph = [[] for _ in range(N+1)]
    tmp = 0

    for _ in range(M):
        A,B,D = map(int,input().split())
        if (B == G and A == H) or (B == H and A == G):
           tmp = D
        graph[A].append((B,D))
        graph[B].append((A,D))

    for _ in range(T):
        t = int(input())
        t_lst.append(t)


    def dijkstra(start):
        distance = [int(1e9)] * (N + 1)
        hq = []

        distance[start] = 0
        heapq.heappush(hq, (0, start))

        while hq:
            dist, now_node = heapq.heappop(hq)

            if dist > distance[now_node]:
                continue

            for next_node, cost in graph[now_node]:
                if distance[next_node] > dist + cost:
                    distance[next_node] = dist + cost
                    heapq.heappush(hq,(dist+cost, next_node))

        return distance



    def dijkstra1(start, end):
        distance = [int(1e9)] * (N + 1)
        hq = []

        distance[start] = 0
        heapq.heappush(hq, (0, start))

        while hq:
            dist, now_node = heapq.heappop(hq)

            if dist > distance[now_node]:
                continue

            for next_node, cost in graph[now_node]:
                if distance[next_node] > dist + cost:
                    distance[next_node] = dist + cost
                    heapq.heappush(hq, (dist + cost, next_node))


        return distance[end]

    def dijkstra2(start, end):
        distance = [int(1e9)] * (N + 1)
        hq = []

        distance[start] = 0
        heapq.heappush(hq, (0, start))

        while hq:
            dist, now_node = heapq.heappop(hq)

            if dist > distance[now_node]:
                continue

            for next_node, cost in graph[now_node]:
                if distance[next_node] > dist + cost:
                    if (next_node == G and now_node == H) or (next_node == H and now_node == G):
                        distance[next_node] = dist + cost - tmp
                        heapq.heappush(hq, (dist + cost - tmp, next_node))

                    else:
                        distance[next_node] = dist + cost
                        heapq.heappush(hq, (dist + cost, next_node))

        return distance[end]


    # 기존 최단거리
    origin_distance = dijkstra(S)


    G_start = dijkstra2(S,G) + tmp
    H_start = dijkstra2(S,H) + tmp
    result = []

    H_to_i = dijkstra(H)
    G_to_i = dijkstra(G)


    for i in t_lst:


        if G_start + H_to_i[i] == origin_distance[i]:
            result.append(i)

        elif H_start + G_to_i[i] == origin_distance[i]:
            result.append(i)

    result.sort()

    print(*result)