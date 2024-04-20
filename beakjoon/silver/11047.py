import sys
input = sys.stdin.readline
n, m = map(int, input().split())

coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)
cnt = 0
for i in coin:

    if m // i > 0:
        cnt += m // i
        m = m % i

    elif m < 0:
        break

print(cnt)