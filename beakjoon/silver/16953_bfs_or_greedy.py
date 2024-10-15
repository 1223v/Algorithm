import sys
from collections import deque
input = sys.stdin.readline

a, b = map(str,input().split())
integerB = int(b)
def bfs(n, num):

    queue = deque()
    queue.append((num,n))

    while queue:
        (x,m) = queue.popleft()

        if int(x+"1") == integerB or int(x) * 2 == integerB:

            print(m+1)
            exit()

        # 1을 뒤에 붙이는 경우
        if int(x+"1") < integerB:
            queue.append((x+"1", m+1))


        # 2을 곱함
        if int(x) * 2 < integerB:
            queue.append((str(int(x) * 2),m+1))


    print(-1)






bfs(1,a)