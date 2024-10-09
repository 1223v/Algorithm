import sys
input = sys.stdin.readline

n,k = map(int,input().split())
s = [i for i in range(1,n+1)]
result = []
idx = 0
while s:
    idx += k-1
    if idx >= len(s):
        idx %= len(s)
    result.append(s.pop(idx))

print("<"+ ", ".join(map(str,result))+">")