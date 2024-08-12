import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph=[[0]* n for _ in range(n)]
number = 2
x = n//2
y = n//2
graph[x][y] =1
repeat = 1
i = 0

answer = [x+1, y+1]
while x != 0 or y != 0:
    flag = 0
    for _ in range(2):
        for _ in range(repeat):
            x += dx[i]
            y += dy[i]
            graph[x][y] = number

            if number == m:
                answer = [x+1, y+1]

            if x == 0 and y == 0:
                flag = 1
                break

            number += 1
        if flag == 1:
            break
        i = (i+1) % 4
    repeat += 1

for i in graph:
    print(*i)

print(*answer)
