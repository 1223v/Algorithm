import sys
input = sys.stdin.readline
import heapq

TC = int(input())

for _ in range(TC):
    N,M,T = map(int,input().split())
    S,G,H = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    t_lst = []
    H_to_G = 0
    for _ in range(M):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
        if (a == H and b == G) or (a == G and b == H):
            H_to_G = d

    for _ in range(T):
        t = int(input())
        t_lst.append(t)


    def dijkstra(start):
        distance = [int(1e9)] * (N+1)
        hq = []

        distance[start] = 0
        heapq.heappush(hq,(0, start))

        while hq:
            dist, now_node = heapq.heappop(hq)

            for next_node, cost in graph[now_node]:
                if distance[next_node] > dist + cost:
                    distance[next_node] = dist + cost
                    heapq.heappush(hq,(dist+cost, next_node))

        return distance


    def dijkstra1(start):
        distance = [int(1e9)] * (N + 1)
        hq = []

        distance[start] = 0
        heapq.heappush(hq, (0, start))

        while hq:
            dist, now_node = heapq.heappop(hq)

            for next_node, cost in graph[now_node]:
                if distance[next_node] > dist + cost:
                    if (next_node == H and now_node == G) or ( next_node == G and now_node == H):
                        distance[next_node] = dist + cost - H_to_G
                        heapq.heappush(hq, (dist + cost - H_to_G, next_node))
                    else:
                        distance[next_node] = dist + cost
                        heapq.heappush(hq, (dist + cost, next_node))

        return distance

    Origin_dist = dijkstra(S)
    S_to = dijkstra1(S)
    S_to_H = S_to[H]
    S_to_G = S_to[G]

    G_dist = dijkstra(G)
    H_dist = dijkstra(H)

    result = []
    for i in t_lst:
        H_G_to_t = S_to_H + H_to_G + G_dist[i]
        G_H_to_t = S_to_G + H_to_G + H_dist[i]

        if H_G_to_t == Origin_dist[i]:
            result.append(i)

        elif G_H_to_t == Origin_dist[i]:
            result.append(i)

    result.sort()
    print(*result)


