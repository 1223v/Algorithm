import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n+1)
s = []

def dfs():
    if m == len(s):
        print(' '.join(map(str,s)))

    for i in range(1, n+1):
        if visited[i] == True:
            continue

        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

dfs()

