import sys
input = sys.stdin.readline

N = int(input())
k = int(input())
s = []
result = []

visited = [False] * N

for i in range(N):
    x = int(input())
    s.append(x)

def dfs(n, v):
    global result
    if n == k:
        result.append(v)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n+1, v+str(s[i]))
            visited[i] = False



dfs(0, "")
set_result = set(result)
print(len(set_result))