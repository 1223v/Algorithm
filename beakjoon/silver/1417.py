import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []
target = 0
for i in range(N):
    tmp = int(input())
    if i == 0:
        target = tmp
    else:
        heapq.heappush(hq, -(tmp))

cnt = 0
while True:
    if len(hq):
        if target > -hq[0]:
            print(cnt)
            break

        elif target <= -hq[0]:
            x = heapq.heappop(hq)
            x = -x -1
            target += 1
            heapq.heappush(hq,-x)
            cnt += 1
    else:
        print(0)
        break