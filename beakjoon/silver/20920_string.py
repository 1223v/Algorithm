import sys
input = sys.stdin.readline

n,m = map(int,input().split())


sos = []
tmp = {}
for i in range(n):
    s = input().rstrip()
    if len(s) >= m:
        if s not in tmp:
            tmp[s] = 1
        else:
            tmp[s] += 1


sos = sorted(tmp.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(sos)):
    print(sos[i][0])


    