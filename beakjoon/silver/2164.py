import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1:
    myQueue.popleft()
    myQueue.append(myQueue.popleft()) # 맨위의 카드를 가장 아래 카드 밑으로 이동

print(myQueue[0])