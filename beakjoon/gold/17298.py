import sys
input = sys.stdin.readline

n = int(input())
ans = [-1] * n # 0이 아닌 -1로 진행하면 마지막 주석된 while문 제거 가능 
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]: # 오큰수 조건
        ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    myStack.append(i)

# while myStack:
#     ans[myStack.pop()] = -1

# result = ""
# for i in range(n):
#     result += str(ans[i])+" "

print(*ans)

# print(result)