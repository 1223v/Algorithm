import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [0] * (N+1)

for i in range(N):
    numbers = list(map(int, input().split()))
    s = numbers[0]
    index = 0
    index += 1

    while True:
        u = numbers[index]

        if u == -1:
            break
        v = numbers[index + 1]
        A[s].append((u,v))
        index += 2

def dfs(v):
    visited[v] = True

    for i in A[v]:
        if not visited[i[0]]:
            visited[i[0]] = True
            distance[i[0]] = distance[v] + i[1]
            dfs(i[0])

dfs(1)
max_value = max(distance)
max_index = distance.index(max_value)
visited = [False] * (N+1)
distance = [0] * (N+1)
dfs(max_index)
print(max(distance))


