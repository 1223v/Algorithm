import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))

