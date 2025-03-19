import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
visited = [0] * N
min_value = float('inf')
def dfs(L,idx):
    global min_value

    if L == N//2:
        A,B = 0,0

        for i in range(N):
            for j in range(N):
                if visited[i] == 1 and visited[j] == 1:
                    A += graph[i][j]

                elif visited[i] == 0 and visited[j] == 0:
                    B += graph[i][j]

        min_value = min(min_value,abs(A-B))


    for i in range(idx, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(L+1, i+1)
            visited[i] = 0


dfs(0,0)
print(min_value)