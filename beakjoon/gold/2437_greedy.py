import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))
s.sort()
min_value = int(1e9)
print(s)

