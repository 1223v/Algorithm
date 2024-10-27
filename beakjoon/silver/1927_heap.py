import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())

    if x > 0:
        hq.heappush(heap,x)

    else:
        if len(heap) > 0:
            print(hq.heappop(heap))
        else:
            print(0)