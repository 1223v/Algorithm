import sys
n, m = map(int, sys.stdin.readline().split())

if n*m <= 1:
    print(0)

else:
    print(n*m -1)