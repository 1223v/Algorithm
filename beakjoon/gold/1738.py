import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [-float('inf')] * (N+1)
path = [0] * (N+1)

for _ in range(M):
    s,e,cost = map(int,input().split())
    graph[s].append((e,cost))

def bf(start):
    distance[start] = 0

    for i in range(N):
        for j in range(1,N+1):
            for e,cost in graph[j]:

                if distance[e] < distance[j] + cost and distance[j] != -float('inf'):
                    distance[e] = distance[j] + cost
                    path[e] = j
                    if i == N-1:
                        distance[e] = float('inf')

    if distance[N] == float('inf'):
        return -1

    k = N
    result = []
    while k != 1:
        result.append(k)
        k = path[k]

    result.append(k)
    result = result[::-1]

    return result



res = bf(1)
if res == -1:
    print(-1)
else:
    print(*res)