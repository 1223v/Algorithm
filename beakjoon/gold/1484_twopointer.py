# 현재 성원이 몸무게 ^ 2 - 성원이가 기억하는 몸무게 ^ 2 = G
import sys
input = sys.stdin.readline
result = []

G = int(input())

now_weight = [i for i in range(1,100001)]


start = 0
end = 1

while start < end:

    tmp = (now_weight[end] * now_weight[end]) - (now_weight[start] * now_weight[start])

    if tmp == G:
        result.append(now_weight[end])
        start += 1


    elif tmp > G:
        start += 1

    else:
        end += 1


result.sort()

if result:
    for i in result:
        print(i)

else:
    print(-1)