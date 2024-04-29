# 1의 자리 숫자가 소수를 결정하는데 요인이 되지는 않음. 하지만 2의 경우는 무조건 나눠지기에 소수는 불가능

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())


def isPrime(number):
    for i in range(2, int(number/2 + 1)):
        if number % i == 0:
            return False
    return True


def DFS(num):
    if len(str(num)) == N:
        print(num)
        return

    for i in range(1,10):
        if i % 2 == 0:
            continue
        if isPrime(num * 10+i):
            DFS(num * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)