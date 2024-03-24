import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def check(num):
    if num == 1:
        return False
    # int(i ** 1/2)제곱근까지만 나눠봐도 소수임을 판단 가능 36의 경우 1,2,3,4,5,6 까지 나눠보고 소수 판단 가능
    for j in range(2, int(num ** 0.5) + 1): # 최대한 소수점을 쓸것
        if i % j == 0:
            return False

    else:
        return True

for i in range (n, m+1):
    if check(i):
        print(i)