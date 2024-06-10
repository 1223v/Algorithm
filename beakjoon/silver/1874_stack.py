import sys

# pop의 경우 버릴수 없으므로 pop할 떄는 무조건 값이 사용되어야 함

input = sys.stdin.readline

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]

    if su >= num:
        while su >= num:

            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"

    else:
        n = stack.pop()
        if n > su:
            result = False
            print("NO")
            break
        else:
            answer += "-\n"

if result:
    print(answer)