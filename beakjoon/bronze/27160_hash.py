import sys
input = sys.stdin.readline

N = int(input())

f_dict = {}

for _ in range(N):
    f, count = map(str,input().split())
    if f in f_dict:
        f_dict[f] += int(count)

    else:
        f_dict[f] = int(count)

for f,count in f_dict.items():
    if count == 5:
        print("YES")
        break
else:
    print("NO")
