import sys
input = sys.stdin.readline

N = int(input())

start = 1
end = 2
result = []

# N = 현재 몸무게 ** 2 - 기억하는 몸무게 ** 2
# 현재 몸무게 > 기억하는 몸무게
while start < end:

    tmp = ((end) ** 2 - (start) ** 2)
    if N == tmp:
        result.append(end)
        end += 1
        start += 1

    elif N > tmp:
        end += 1

    elif N < tmp:
        start += 1

if len(result) > 0:
    for i in result:
        print(i)

else:
    print(-1)
