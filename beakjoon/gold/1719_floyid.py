import sys
input = sys.stdin.readline

N,M = map(int,input().split())
distance = [[float('inf')] * (N+1) for _ in range(N+1)]
graph = [[0] * (N+1) for _ in range(N+1)]


for _ in range(M):
    s,e,cost = map(int,input().split())

    if distance[s][e] > cost:
        distance[s][e] = cost
        graph[s][e] = e
    if distance[e][s] > cost:
        distance[e][s] = cost
        graph[e][s] = s

def floyid():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

                    graph[i][j] = graph[i][k]



floyid()

for i in range(1,N+1):
    for j in range(1,N+1):
        if float('inf') <= distance[i][j] or i==j:
            print('-',end=' ')

        else:
            print(graph[i][j],end=' ')

    print()




