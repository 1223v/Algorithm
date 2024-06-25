import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True

def bfs(num):
    queue = deque()
    queue.append(num)
    while queue:
        x = queue.popleft()
        if len(str(x)) == N:
            print(x)

        else:
            for i in range(1,10):
                if isPrime(x*10 + i):
                    queue.append(x*10+i)

bfs(2)
bfs(3)
bfs(5)
bfs(7)