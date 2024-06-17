import sys
from queue import PriorityQueue
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str(temp[1])+'\n')

    else:
        # 우선순위 큐는 (우선순위, 값)으로 put할 경우 우선순위 기준으로 정렬되고 우선순위가 같은 경우 값 기준으로 정렬함
        myQueue.put((abs(request), request))

