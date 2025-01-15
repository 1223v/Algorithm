import sys
input = sys.stdin.readline

N = int(input())
target = abs(100-N)
M = int(input())
num = list(map(int,input().split()))


for i in range(100001):
    number = str(i)
    for j in range(len(number)):
        if int(number[j]) in num:
            break

        elif j == len(number)-1:

            target = min(target, len(number) + abs(i-N))

print(target)