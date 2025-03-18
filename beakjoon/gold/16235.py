import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
graph = [[5] * N for _ in range(N)]
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

tree = [[{} for _ in range(N)] for _ in range(N)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    tree[X-1][Y-1].append(Z)


for _ in range(K):

    for i in range(N):
        for j in range(N):
            tree[i][j].sort()
            for k in range(len(tree[i][j])):
                if tree[i][j][k] <= graph[i][j]:
                    graph[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1

                else:
                    while k < len(tree[i][j]):
                        graph[i][j] += (tree[i][j].pop() // 2)

                    break

    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for x in range(8):
                        ni,nj = i + di[x], j + dj[x]
                        if 0 <= ni < N and 0<= nj < N:
                            tree[ni][nj].append(1)


    for i in range(N):
        for j in range(N):
            graph[i][j] += A[i][j]



ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])

print(ans)


