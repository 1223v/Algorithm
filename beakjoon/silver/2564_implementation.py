import sys
input = sys.stdin.readline

Col,Row = map(int,input().split())

total = 0
s_lst = []
store = int(input())
for _ in range(store):
    direction, point = map(int,input().split())
    s_lst.append((direction, point))

x,y = map(int,input().split())

def cal(dir, dist):
    if dir == 1:
        return dist
    elif dir == 2:
        return Col + Row + (Col - dist)
    elif dir == 3:
        return Col + Row + Col + (Row - dist)
    else:
        return Col + dist

dist1 = cal(x,y)
for i in range(store):
    dist2 = cal(s_lst[i][0],s_lst[i][1])
    path1 = abs(dist1 - dist2)
    path2 = Col + Col + Row + Row - path1
    total += min(path1, path2)

print(total)
