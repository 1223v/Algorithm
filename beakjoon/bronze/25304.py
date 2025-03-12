import sys
input = sys.stdin.readline

total = int(input())
amount = int(input())
A = [list(map(int,input().split())) for _ in range(amount)]

result = 0
for i in range(amount):
    result += A[i][0] * A[i][1]

if total == result:
    print("Yes")

else:
    print("No")

