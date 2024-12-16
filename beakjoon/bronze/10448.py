import sys
input = sys.stdin.readline

TC = int(input())
lst = [n*(n+1) // 2 for n in range(1,46)]
result = [0] * 1001

for i in lst:
    for j in lst:
        for t in lst:
            if i+j+t <= 1000:
                result[i+j+t] = 1

for _ in range(TC):
    N = int(input())
    print(result[N])


