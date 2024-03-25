import sys

input = sys.stdin.readline

n = int(input())

AL = [list(map(int,input().split())) for _ in range(n)]

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x%y)

for i in range(n):
    result = (AL[i][0]*AL[i][1]) // gcd(AL[i][0], AL[i][1])
    print(result)