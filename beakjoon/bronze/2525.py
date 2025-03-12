import sys
input = sys.stdin.readline

h,m = map(int, input().split())
tm = int(input())

result = h * 60 + m + tm
print((result//60)%24, result%60)