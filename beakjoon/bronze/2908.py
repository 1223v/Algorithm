import sys
input = sys.stdin.readline

n,m = map(str,input().split())

x = int(n[::-1])
y = int(m[::-1])

print(x if x > y else y)
