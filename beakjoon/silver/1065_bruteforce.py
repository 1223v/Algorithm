import sys
input = sys.stdin.readline

N = int(input())
result = 0

for i in range(1,N+1):
    slst = list(map(int,str(i)))
    if i < 100:
        result += 1
    elif slst[0] - slst[1] == slst[1] - slst[2]:
        result += 1

print(result)

