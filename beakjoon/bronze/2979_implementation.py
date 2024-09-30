import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
total = [0]*100
cost = 0
for _ in range(3):
    x,y = map(int,input().split())
    for i in range(x,y):
        total[i] += 1

for i in total:
    if i == 3:
        cost += c*3
    elif i == 2:
        cost += b*2
    elif i == 1:
        cost += a


print(cost)