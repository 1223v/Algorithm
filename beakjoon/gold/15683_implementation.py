import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s = [[6] * (M+2)]+[[6] + list(map(int,input().split())) + [6] for _ in range(N)] + [[6] * (M+2)]

lst = []
min_value = N*M
cctv = [[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]
di =[0,1,0,-1]
dj = [1,0,-1,0]

def cal(tlst):
    visited = [[0] * (M+2) for _ in range(N+2)]
    for i in range(CNT):
        si,sj = lst[i]
        rot = tlst[i]
        ans = s[si][sj]

        for dr in cctv[ans]:
            ci,cj = si,sj
            dr = (dr + rot) %4
            while True:

                ci = ci + di[dr]
                cj = cj + dj[dr]
                if s[ci][cj] == 6:
                    break
                visited[ci][cj] = 1

    count = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if s[i][j] == 0 and visited[i][j] == 0:
                count += 1

    return count


def dfs(n,tlst):
    global min_value
    if CNT == n:
        min_value = min(min_value, cal(tlst))
        return

    dfs(n+1, tlst+[0])
    dfs(n + 1, tlst + [1])
    dfs(n + 1, tlst + [2])
    dfs(n + 1, tlst + [3])

for i in range(1,N+1):
    for j in range(1,M+1):
        if 1 <= s[i][j] < 6:
            lst.append((i,j))


CNT = len(lst)
dfs(0,[])
print(min_value)