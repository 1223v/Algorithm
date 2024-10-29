import sys
input = sys.stdin.readline

N, L, W, H = map(int,input().split())

start = 0
end = max(L, W, H)
result = 0
for _ in range(10000):
    mid = (start + end) / 2
    if (L//mid)*(W//mid)*(H//mid) >= N:
        start = mid
        result = mid

    else:
        end = mid

print(result)