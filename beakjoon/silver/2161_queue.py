import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
s = deque([i for i in range(1,N+1)])
result = []
while len(s) > 1:
    result.append(s.popleft())
    s.append(s.popleft())

if len(s) == 1:
    result.append(s.popleft())

print(*result)