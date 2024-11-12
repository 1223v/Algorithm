#https://www.acmicpc.net/problem/2847
import sys
input = sys.stdin.readline

N = int(input())
score = []
for i in range(N):
    score.append(int(input()))
cnt = 0
for i in range(N-1,0,-1):
    if score[i] <= score[i-1]:
        cnt += score[i-1] - score[i] + 1
        score[i - 1] = score[i] - 1

print(cnt)