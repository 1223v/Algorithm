import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = [0] + [i for i in range(1,n+1)]

for i in range(m):
    x,y = map(int,input().split())
    o= s[y]
    p= s[x]
    s[x] = o
    s[y] = p

for i in range(1,n+1):
    print(s[i], end=' ')

