#https://www.acmicpc.net/problem/1987
import sys
from collections import defaultdict
input = sys.stdin.readline

R,C = map(int,input().split())

s = [list(map(str, input().rstrip())) for _ in range(R)]
alpha_lst = defaultdict(int)
di = [-1,1,0,0]
dj = [0,0,-1,1]
max_value = 0

def dfs(n,ci,cj):
    global max_value

    for i in range(4):
        ni,nj = ci+di[i], cj+dj[i]
        if 0 <= ni < R and 0 <= nj < C:
            if alpha_lst[s[ni][nj]] == 0:
                alpha_lst[s[ni][nj]] = 1
                dfs(n+1, ni,nj)
                alpha_lst[s[ni][nj]] = 0

    max_value = max(n, max_value)


def dfs2(n,ci,cj, history):
    global max_value

    for i in range(4):
        ni,nj = ci+di[i], cj+dj[i]
        if 0 <= ni < R and 0 <= nj < C:
            if s[ni][nj] not in history:
                dfs2(n+1, ni,nj, history + s[ni][nj])


    max_value = max(n, max_value)

alpha_lst[s[0][0]] = 1
dfs(1,0,0)
#dfs2(1,0,0,s[0][0])
print(max_value)

