import sys
input = sys.stdin.readline

n = int(input())
visited = [False] * (n+1)

def dfs(s):

    if len(s) == n:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            dfs(s+str(i))
            visited[i] = False


dfs("")