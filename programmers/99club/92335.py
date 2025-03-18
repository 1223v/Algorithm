import math
def isPrime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

        # 제곱근까지만 검사
    for i in range(5, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    tmp = ""


    while n > 0:

        mod = n % k
        n = n // k
        tmp += str(mod)


    cnt = 0

    tmp = tmp[::-1]
    # 소수 2,3,5,7
    for i in tmp.split('0'):


        if i == "":
            continue
        if isPrime(int(i)):
            cnt += 1

    return cnt



print(solution(437674,3))