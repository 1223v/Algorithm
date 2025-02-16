import sys
import heapq
input = sys.stdin.readline

N = int(input())
s = sorted([list(map(int,input().split())) for _ in range(N)])
hq = []
for start, end in s:
    if hq and hq[0] <= start:
        heapq.heappop(hq)
    heapq.heappush(hq,end)

print(len(hq))
