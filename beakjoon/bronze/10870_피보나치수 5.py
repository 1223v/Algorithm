import sys
input = sys.stdin.readline

def fibo(x):
    if x <= 1: # 기저 조건 fibo(1) = 1이며, fibo(0) = 0이다
        return x
    return fibo(x-1)+fibo(x-2)


x = int(input())
print(fibo(x))