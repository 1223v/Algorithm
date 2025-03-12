import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []

for i in range(N):
    s = list(map(int,input().split()))

    for j in s:

        if len(hq) < N:
            heapq.heappush(hq, j)
        else:
            if j > hq[0]:

                heapq.heappop(hq)
                heapq.heappush(hq,j)


print(hq[0])
