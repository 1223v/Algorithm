import sys
input = sys.stdin.readline

N, P, Q = map(int,input().split())
s = {}

def dfs(n):
    if n in s:
        return s[n]
    else:
        s[n] = dfs(n//P) + dfs(n//Q)
        return s[n]


s[0] = 1
dfs(N)

print(s[N])