import sys
input = sys.stdin.readline

n = int(input())
s = []
score = 0
A_time = 0
B_time = 0
for _ in range(n):
    x, y = map(str,input().split())
    m = y.split(':')
    tim = int(m[0]) * 60 + int(m[1])


    if score > 0:
        A_time += tim - s[-1]


    elif score < 0:
        B_time += tim - s[-1]

    else:
        pass

    if int(x) == 1:
        score += 1
    else:
        score -= 1

    if len(s) == 0:
        s.append(tim)
        continue

    s.append(tim)


if score > 0:
    A_time += 2880 - s[-1]

elif score < 0:
    B_time += 2880 - s[-1]


A_min, A_sec = divmod(A_time, 60)
B_min, B_sec = divmod(B_time, 60)
print(f"{A_min:02}:{A_sec:02}")
print(f"{B_min:02}:{B_sec:02}")


