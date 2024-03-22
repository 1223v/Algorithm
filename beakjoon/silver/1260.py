def bfs(s):
    queue = [] # 필요한것 : queue, visited2, 변수
    queue.append(s)
    ans_bfs.append(s) # pop 역할
    visited2[s] = 1
    while queue:
        c = queue.pop(0)
        for n in adj[c]:
            if not visited2[n]:
                queue.append(n)
                ans_bfs.append(n)
                visited2[n] = 1

def dfs(c):
    ans_dfs.append(c) # pop 역할
    visited1[c] = 1
    for n in adj[c]:
        if not visited1[n]:
            dfs(n)

N, M, V = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

visited1 = [0] * (N+1)
ans_dfs = []
dfs(V)

visited2 = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)