def solution(n, k):
    answer = -1

    def isPrime(num):

        if num == 1:
            return False
        for i in range(2,int(num**(0.5))+1):
            if num % i == 0:

                return False
        return True

    tmp = ""

    while n > 0:
        mod = n %k
        n = n // k
        tmp += str(mod)


    tmp = tmp[::-1]
    cnt = 0
    for i in tmp.split('0'):

        if i != "" and isPrime(int(i)):
            cnt += 1


    return cnt

print(solution(437674,3))