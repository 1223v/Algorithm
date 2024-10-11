import sys
input = sys.stdin.readline

N = int(input())
visited = [False] * N
s = list(map(int, input().split()))
x = [[] for _ in range(N)]
min_value = sys.maxsize
for i in range(N):
    count = int(input())
    for _ in range(count):
        ci,pi = map(int,input().split())
        x[i].append((ci-1,pi))

def check(v):
    if v <= 0:
        return 1
    else:
        return v

def dfs(n,total):
    global min_value

    if n == N:
        min_value = min(min_value, total)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            for xi,yi in x[i]:
                s[xi] -= yi
            dfs(n+1, total+check(s[i]))
            for xi,yi in x[i]:
                s[xi] += yi
            visited[i] = False

dfs(0,0)
print(min_value)