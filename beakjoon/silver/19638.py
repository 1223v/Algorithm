# https://www.acmicpc.net/problem/19638
import heapq
import sys
input = sys.stdin.readline

N, H, T = map(int,input().split())

A = []
for _ in range(N):
    heapq.heappush(A,-(int(input())))
cnt = 0
for i in range(T):

    if H > abs(A[0]) or abs(A[0]) == 1:
        break
    if abs(A[0]) >= H and abs(A[0]) > 1:
        x = heapq.heappop(A)
        realx = abs(x)
        heapq.heappush(A,-(int(realx / 2)))
        cnt += 1


if abs(A[0]) >= H:
    print("NO")
    print(abs(A[0]))
else:
    print("YES")
    print(cnt)