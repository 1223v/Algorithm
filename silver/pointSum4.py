import sys
n, m = map(int, sys.stdin.readline().split())
totals = list(map(int, sys.stdin.readline().split()))
sections_sum = []

sum = 0
for i in totals:
    sum += i
    sections_sum.append(sum)

numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


for i in range(m):

    if numbers[i][0]-2 < 0:
        print(sections_sum[numbers[i][1] - 1])
    else:
        print(sections_sum[numbers[i][1]-1] - sections_sum[numbers[i][0]-2])

