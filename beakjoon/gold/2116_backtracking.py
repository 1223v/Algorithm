import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
s = [list(map(int, input().split())) for _ in range(N)]
max_value = 0

def dfs(n,k,total):
    global max_value
    if n == N:
        max_value = max(max_value, total)
        return

    x = s[n].index(k)
    if x == 0:
        dfs(n+1,s[n][5], total+max(s[n][1],s[n][2],s[n][3],s[n][4]))
    elif x == 1:
        dfs(n+1,s[n][3], total+max(s[n][0],s[n][2],s[n][4],s[n][5]))
    elif x == 2:
        dfs(n+1,s[n][4], total+max(s[n][0],s[n][1],s[n][3],s[n][5]))
    elif x == 3:
        dfs(n+1,s[n][1], total+max(s[n][0],s[n][2],s[n][4],s[n][5]))
    elif x == 4:
        dfs(n+1,s[n][2], total+max(s[n][0],s[n][1],s[n][3],s[n][5]))
    elif x == 5:
        dfs(n+1,s[n][0], total+max(s[n][1],s[n][2],s[n][3],s[n][4]))


for i in range(N):
    if i == 0:
        dfs(1,s[0][5], max(s[0][1],s[0][2],s[0][3],s[0][4]))
    elif i == 1:
        dfs(1,s[0][3], max(s[0][0],s[0][2],s[0][4],s[0][5]))
    elif i == 2:
        dfs(1,s[0][4], max(s[0][0],s[0][1],s[0][3],s[0][5]))
    elif i == 3:
        dfs(1,s[0][1], max(s[0][0],s[0][2],s[0][4],s[0][5]))
    elif i == 4:
        dfs(1,s[0][2], max(s[0][0],s[0][1],s[0][3],s[0][5]))
    elif i == 5:
        dfs(1,s[0][0], max(s[0][1],s[0][2],s[0][3],s[0][4]))


print(max_value)