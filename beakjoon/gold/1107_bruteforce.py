import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))
count = 0
for i in range(N):
    start = 0
    end =