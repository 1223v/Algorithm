import sys
input = sys.stdin.readline

n = int(input())
x_stack = []
for _ in range(n):
    command = input().rstrip()

    first_command = command.split()

    if first_command[0] == "1":
        x_stack.append(int(first_command[1]))

    elif first_command[0] == "2":
        if len(x_stack) > 0:
            k=x_stack.pop()
            print(k)
        else:
            print(-1)

    elif first_command[0] == "3":
        print(len(x_stack))

    elif first_command[0] == "4":
        if len(x_stack) > 0:
            print(0)
        else:
            print(1)

    elif first_command[0] == "5":
        if len(x_stack) > 0:
            print(x_stack[-1])
        else:
            print(-1)
