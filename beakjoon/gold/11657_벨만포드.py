import sys
input = sys.stdin.readline

N,M = map(int,input().split())

edges = []
distance = [float('inf')] * (N+1)

def bf(start):
    distance[start] = 0

    for i in range(N):
        for j in range(M):
            s,e,cost = edges[j]
            if distance[e] > distance[s] + cost:
                distance[e] = distance[s] + cost
                if i == N-1:
                    return True
    return False

for _ in range(M):
    a,b,cost = map(int,input().split())
    edges.append((a,b,cost))


chk = bf(1)

if chk:
    print(-1)

else:
    for i in range(2,N+1):
        if distance[i] != float('inf'):
            print(distance[i])
        else:
            print(-1)
