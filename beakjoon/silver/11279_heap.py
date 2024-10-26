import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    x = int(input())

    if x > 0:
        hq.heappush(heap,(-x,x))
    else:
        if len(heap) > 0:
            print(hq.heappop(heap)[1])
        else:
            print(0)
