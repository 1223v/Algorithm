import sys

n = int(sys.stdin.readline())
people = sorted(list(map(int,input().split())))
total = 0
sum_list = []
for i in people:
    total += i
    sum_list.append(total)
print(sum(sum_list))