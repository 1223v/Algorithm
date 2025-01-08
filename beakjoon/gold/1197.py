import sys
from queue import PriorityQueue
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N,M = map(int,input().split())
parent = [i for i in range(N+1)]

pq = PriorityQueue()
for _ in range(M):
    s,e,w = map(int,input().split())
    pq.put((w,s,e))

result = 0
useEdge = 0

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

while useEdge < N-1:
    w,s,e = pq.get()
    if find(s) != find(e):

        union(s,e)
        result += w
        useEdge += 1

print(result)