#https://www.acmicpc.net/problem/1374

import sys
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]
s.sort(key=lambda x : x[1])
hq = []
cnt = 0
for i in s:

    while hq and hq[0] <= i[1]:
        heapq.heappop(hq)
    heapq.heappush(hq,i[2])
    cnt = max(cnt, len(hq))

print(cnt)

# queue = deque()
# for i in s:
#
#     while queue and queue[0] <= i[1]:
#         queue.popleft()
#     queue.append(i[2])
#     sorted(queue)
#     cnt = max(cnt,len(queue))
# print(cnt)