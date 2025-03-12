import sys
input = sys.stdin.readline

n = int(input())
num_stack = []
def push(x):
    num_stack.append(x)
def pop():
    if len(num_stack) >0:
        x= num_stack.pop()
        print(x)
    else:
        print(-1)

def size():
    print(len(num_stack))

def empty():
    if len(num_stack) >0:
        print(0)
    else:
        print(1)

def top():
    if len(num_stack) >0:
        print(num_stack[-1])
    else:
        print(-1)

for _ in range(n):
    s = input().rstrip()
    slst = s.split()

    if "push" == slst[0]:
        push(slst[1])
    elif "pop" == slst[0]:
        pop()
    elif "size" == slst[0]:
        size()
    elif "empty" == slst[0]:
        empty()
    elif "top" == slst[0]:
        top()
