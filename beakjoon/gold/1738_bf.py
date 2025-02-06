import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = []
distance = [-float('inf')] * (N+1)
put = [0] * (N+1)

for _ in range(M):
    s,e,cost = map(int,input().split())
    graph.append((s,e,cost))


def bf(start):

    distance[start] = 0

    for i in range(N):
        for s,e,cost in graph:
            if distance[e] < distance[s] + cost and distance[s] != -float('inf'):
                distance[e] = distance[s] + cost
                put[e] = s
                if i == N-1:
                    distance[e] = float('inf')

    if distance[N] == float('inf'):
        return -1

    k = N
    res = []
    while k != 1:
        res.append(k)
        k = put[k]
    res.append(k)
    res = res[::-1]
    return res

result = bf(1)

if result == -1:
    print(-1)

else:
    print(*result)
