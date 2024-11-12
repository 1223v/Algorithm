T = int(input())

def dfs(n,total):
    global min_value
    if total > min_value:
        return
    if n == N:
        min_value = min(min_value,total)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n+1,total+s[n][i])
            visited[i] = False



for test_case in range(1,T+1):

    N = int(input())
    s = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N
    min_value = int(1e9)

    dfs(0,0)
    print(f"#{test_case} {min_value}")

