import sys
input = sys.stdin.readline

N,M = map(int,input().split())

parent = [i for i in range(N+1)]

def find(a):
    if a == parent[a]:
        return a

    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def chksum(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        print("YES")
    else:
        print("NO")

for _ in range(M):
    chk, a, b = map(int,input().split())
    if chk == 0:
        union(a,b)

    if chk == 1:
        chksum(a,b)
