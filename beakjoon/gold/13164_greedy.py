import sys
input = sys.stdin.readline

# 두명으로 묶는 것이 최대한 많이 빼기 때문에 효율적 3명으로 묶는경우 뺄 수 있는 경우가 적어짐

n,m = map(int,input().split())
s = list(map(int, input().split()))
result = 0
answer = []
for i in range(1,n):
    answer.append(s[i]-s[i-1])

answer.sort()

for i in range(n-m):
    result += answer[i]

print(result)