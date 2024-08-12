import sys

# input = sys.stdin.readline

n = int(input())
A = [input() for _ in range(n)]

for i in A:
    print(i.lower())
