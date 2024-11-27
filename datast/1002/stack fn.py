capacity = 10
array = [None] * capacity
top = -1

def isEmpty():
    return top==-1

def isFull():
    return top == capacity-1

def push(e):
    global top
    if not isFull():
        top += 1
        array[top] = e

    else:
        print("overflow!!")
        exit()

def pop():
    global top
    if not isEmpty():
        top -= 1
        return array[top+1]
    else:
        print("underflow!!")
        exit()

msg = input("문자열 입력 : ")# 안녕하세요
for i in msg:# 안>녕>하>세>요
    push(i)
print("문자열 출력 : ", end='')
while not isEmpty():
    print(pop(), end='') # 요>세>하>녕>안
print()