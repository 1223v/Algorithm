import sys
input = sys.stdin.readline

N,M,H = map(int,input().split())
graph = [[0] * (N+2) for _ in range(H+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1

pos = []
for i in range(1,H+1):
    for j in range(1,N+1):
        if graph[i][j] == 0:
            pos.append((i,j))

def check():
    for sj in range(1,N+1):
        j = sj
        for i in range(1,H+1):
            if graph[i][j-1] == 1:
                j -= 1
            elif graph[i][j] == 1:
                j+=1

        if sj != j:
            return False

    return True


def dfs(n,s):
    global ans

    if ans == 1:
        return

    if n == cnt:
        if check():
            ans = 1
        return

    for i in range(s, CNT):
        ci,cj = pos[i]

        if graph[ci][cj-1] == 0 and graph[ci][cj+1] == 0:
            graph[ci][cj] = 1
            dfs(n+1, i+1)
            graph[ci][cj] = 0


CNT = len(pos)
for cnt in range(4):
    ans = 0
    dfs(0,0)
    if ans == 1:
        ans = cnt
        break
else:
    ans = -1

print(ans)