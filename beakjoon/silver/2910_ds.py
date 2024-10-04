import sys

input = sys.stdin.readline

length, counts = map(int, input().split())
lst = list(map(int, input().split()))
num_set=[]
for x in lst:
    if x not in num_set:
        num_set.append(x)

lst.sort()
tmp = 0
count = 0
result = [] #(빈도, 나온 순서, 값)

for i in range(length):

    if lst[i] == tmp:
        count += 1

    else:
        if tmp != 0:
            result.append((count, num_set.index(lst[i-1]),tmp))
        tmp = lst[i]
        count = 1

result.append((count, num_set.index(lst[-1]),tmp))


result.sort(key=lambda x: (-x[0],x[1]))

total = ""
for i in range(len(num_set)):
    for j in range(result[i][0]):
        total += str(result[i][2])+" "



print(total.rstrip())



