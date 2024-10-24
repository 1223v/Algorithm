import sys
input = sys.stdin.readline
X = int(input())
count = 0
for i in [64,32,16,8,4,2,1]:
    if X == 0:
        break

    if X >= i:
        X -= i
        count += 1

print(count)

