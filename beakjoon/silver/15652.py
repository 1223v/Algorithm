import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


N, M = map(int,input().split())

visited = [False] * (N+1)
s = []

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N+1):
        # if visited[i] == True:
        #     continue
        #
        # visited[i] = True
        s.append(i)
        dfs(i)
        s.pop()
        # visited[i] = False

dfs(1)