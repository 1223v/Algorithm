import sys
input = sys.stdin.readline

s = [input().rstrip() for _ in range(5)]

m = max(len(s[0]),len(s[1]),len(s[2]),len(s[3]),len(s[4]))
k = 0
while True:
    if m == k:
        exit()
    for i in range(5):
        if len(s[i]) <= k:
            continue

        else:
            print(s[i][k], end='')



    k += 1

