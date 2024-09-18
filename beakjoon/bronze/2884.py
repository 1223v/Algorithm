import sys
input = sys.stdin.readline

n,m = map(int, input().split())

time = n * 60 + m - 45

if time >= 0:
    h = time//60
    m = time%60

else:
    h = (1440 + time) // 60
    m = (1440 + time) % 60

if m == 60:
    m = 0
    h = (h+1)%24

print(h, m, end=' ')