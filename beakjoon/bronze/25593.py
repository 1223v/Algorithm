import sys
input = sys.stdin.readline

N = int(input())
s = {}
for i in range(N ):
    for k in range(4):
        x = input().rstrip().split()
        for j in x:
            if "-" != j:
                if k == 0:
                    if j in s:
                        s[j] += 4
                    else:
                        s[j] = 4

                elif k == 1:
                    if j in s:
                        s[j] += 6
                    else:
                        s[j] = 6

                elif k == 2:

                    if j in s:
                        s[j] += 4
                    else:
                        s[j] = 4

                elif k == 3:

                    if j in s:
                        s[j] += 10
                    else:
                        s[j] = 10


tmp = s.values()

if len(tmp) == 0:
    print("Yes")
else:
    if max(tmp) - min(tmp) <= 12:
        print("Yes")
    else:
        print("No")


