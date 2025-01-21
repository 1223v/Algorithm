import sys
input = sys.stdin.readline

tbl = [[1],[2],[3],[4],[5],[6,21],[7],[8],[9],[10],[11,27], [12], [13], [14], [15],[16,29],[17],[18],[19],[20],[32],[22],[23],[24],[25],[26],[20],[28],[24],[30],[31],[24],[32],[32],[32],[32],[32]]
value = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,30,35,22,24,28,27,26,0]

def dfs(n,sm):
    global ans
    if n == 10:
        ans = max(ans,sm)
        return

    for j in range(4):
        tmp = visited[j]
        c = tbl[tmp][-1]

        for _ in range(1,s[n]):
            c = tbl[c][0]

        if c == 32 or c not in visited:
            visited[j] = c
            dfs(n+1, sm+ value[c])
            visited[j] = tmp


s = list(map(int,input().split()))
visited = [0,0,0,0]

ans = 0
dfs(0,0)
print(ans)
