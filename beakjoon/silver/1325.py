import sys
input = sys.stdin.readline

n,m = map(int, input().split())
A = [[] for _ in range(n+1)]
answer = [[0] * n for _ in range(n+1)]

def bfs(v):
    pass

for _ in range(n):
	u,v = map(int, input().split())
	A[u].append(v)
	

for i in range(1,n+1):
	