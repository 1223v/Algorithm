import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
import heapq

V,E = map(int,input().split())
parent = [i for i in range(V+1)]
hq = []
for _ in range(E):
    s,e,w = map(int,input().split())
    heapq.heappush(hq,(w,s,e))

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




useEdge = 0
result = 0
while useEdge < V -1:
    w,s,e = heapq.heappop(hq)
    if find(s) != find(e):
        union(s,e)
        result += w
        useEdge += 1


print(result)
