import sys

input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]

A.sort(key=lambda x:(x[0],x[1]))

for i in A:
    print(' '.join(map(str,i)))