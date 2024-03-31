import sys
input = sys.stdin.readline

n,m = map(int, input().split())
parent = [i for i in range(n)]
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def unionfunc(a,b):

    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for i in range(m):
    a,b = map(int,input().split())

    if find(a) == find(b):
        print(i +1)
        break
    unionfunc(a,b)

else:
    print(0)