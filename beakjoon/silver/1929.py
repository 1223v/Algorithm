import sys

input = sys.stdin.readline

n, m = map(int, input().split())

for i in range (n, m+1):
    if i == 1:
        continue
    # int(i ** 1/2)제곱근까지만 나눠봐도 소수임을 판단 가능 36의 경우 1,2,3,4,5,6 까지 나눠보고 소수 판단 가능
    for j in range(2, int(i ** 1/2) + 1):
        if i % j == 0:
            break

    else:
        print(i)