import sys
input = sys.stdin.readline

A = list(map(str,input().split('-')))
result = 0
def mySum(v):
    sum = 0
    temp = A[v].split('+')
    for i in temp:
        sum += int(i)

    return sum

for i in range(len(A)):
    sum = mySum(i)
    if i == 0:
        result += sum
    else:
        result -= sum

print(result)