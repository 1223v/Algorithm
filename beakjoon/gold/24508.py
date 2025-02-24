import sys
input = sys.stdin.readline

N,K,T = map(int,input().split())
s = sorted(list(map(int,input().split())))



start = 0
end = N-1
count = 0

while start < end:

    if s[start] == 0:
        start += 1
        continue

    if s[end] == K:
        end -= 1
        continue

    move = min(s[start], K-s[end])
    s[start] -= move
    s[end] += move

    count += move

    if count > T:
        print("NO")
        exit()

if all(x == 0 for x in s):
    print("YES")
else:
    print("NO")
