import sys
input = sys.stdin.readline

s = int(input())
i = 1
count = 0
while True:

    s -= i
    if s < 0:
        break
    i += 1
    count += 1

print(count)
