import time

# 재귀적으로 팩토리얼을 계산하는 함수
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 반복문으로 팩토리얼을 계산하는 함수
def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

values=[3,4,5]  # 큰 값을 사용하여 성능을 비교
for n in values:
    # 재귀적 팩토리얼 함수 시간 측정
    start_recursive = time.time()
    result_recursive = factorial(n)
    end_recursive = time.time()

    # 반복문 팩토리얼 함수 시간 측정
    start_iterative = time.time()
    result_iterative = factorial_for(n)
    end_iterative = time.time()

    # 결과 출력
    print("재귀적 Factorial %d! = %d" % (n, result_recursive))
    print("재귀적 실행시간 = ", end_recursive - start_recursive)

    print("반복문 Factorial %d! = %d" % (n, result_iterative))
    print("반복문 실행시간 = ", end_iterative - start_iterative)
