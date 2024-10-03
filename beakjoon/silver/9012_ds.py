import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    stack = []
    for i in range(len(s)):

        if s[i] == "(":
            stack.append(s[i])
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                print("NO")
                break
    else:

        if len(stack) > 0:
            print("NO")
        else:
            print("YES")