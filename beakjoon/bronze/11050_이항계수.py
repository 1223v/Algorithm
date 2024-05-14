import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def recursion_factorial(n):
    if n == 0:
        return 1
    return n * recursion_factorial(n-1)

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n, k = map(int,input().split())
print(factorial(n) // (factorial(k) * factorial(n-k)))