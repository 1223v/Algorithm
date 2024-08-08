import sys
input = sys.stdin.readline

n,m = map(int, input().split())
A = list(map(int, input().split()))
visited = [False] * n
s = []
A.sort()

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    prev = 0
    for i in range(v,n):
        if not visited[i] and prev != A[i]:
            visited[i] = True
            s.append(A[i])
            prev = A[i]
            dfs(i)
            s.pop()
            visited[i] = False


dfs(0)