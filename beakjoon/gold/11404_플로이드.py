import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [[float('inf')]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    distance[i][i] = 0

for _ in range(M):
    s,e,cost = map(int,input().split())
    if distance[s][e] > cost:
        distance[s][e] = cost

def floyid_func():

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

floyid_func()


for i in range(1,N+1):
    for j in range(1,N+1):
        if distance[i][j] == float('inf'):
            distance[i][j] = 0

        print(distance[i][j],end=' ')
    print()
