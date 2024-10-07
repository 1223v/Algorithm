import sys
input = sys.stdin.readline

n,m = map(int,input().split())
result = []
s = ([[0] *(n+1)]) + [[0] + list(map(int,input().split())) for _ in range(n)]
chicken_home = []
home = []
ans = float('inf')


for i in range(n+1):
   for j in range(n+1):
       if s[i][j] == 2:
           chicken_home.append((i,j))
       elif s[i][j] == 1:
           home.append((i,j))


def cal(tlst):
    global n
    sm = 0
    for hi,hj in home:
        k = float('inf')
        for ci,cj in tlst:
            k = min(k, abs(hi-ci) + abs(hj-cj))
        sm += k
    return sm

def dfs(n, tlst):
    global ans
    if n == cnt:
        if len(tlst) == m:
            ans = min(ans, cal(tlst))
        return

    # 폐업
    dfs(n+1, tlst)

    # 안폐업
    dfs(n+1, tlst+[chicken_home[n]])

cnt = len(chicken_home)
dfs(0,[])

print(ans)
