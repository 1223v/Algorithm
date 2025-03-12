import sys
input = sys.stdin.readline

TD, RL = map(int,input().split())

store = int(input())
s = []
result = 0

for _ in range(store):
    dir, p = map(int,input().split())
    s.append((dir,p))

x,y = map(int,input().split())
def move(dir, dist):
    if dir == 1:
        return dist

    elif dir == 2:
        return TD + RL + (TD-dist)

    elif dir == 3:
        return TD * 2 + RL + (RL - dist)

    elif dir == 4:
        return dist + TD

dist1 = move(x,y)

for i in range(store):
    dist2 = move(s[i][0], s[i][1])
    distance1 = abs(dist1 - dist2)
    distance2 = TD * 2 + RL * 2 - distance1

    result += min(distance1, distance2)

print(result)

