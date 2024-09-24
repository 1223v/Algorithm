import sys
input = sys.stdin.readline

n = int(input())
s = [0]+list(map(int,input().split()))
k = [i for i in range(1,n+1)]

for i in range(n,0,-1):
    if s[i] > 0:
        m = k.index(i)
        k.insert(m+s[i]+1,i)
        k.pop(m)
        s[i] = 0

print(*k)
