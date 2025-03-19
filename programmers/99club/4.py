import math
def solution(n):

    S = [1]


    S[0] = 1
    cnt = 0
    i = 1
    chk = 0
    while True:

        if chk == 1:
            break

        for j in range(i):
            print(S)
            if len(S) >= n:
                chk = 1
                break
            if S[j] == 3**cnt:
                S.append((3 ** (cnt + 1)))
                cnt += 1
                i += 1
                break

            elif 3 ** cnt <= S[j] + (3**cnt) <= 3 ** (cnt+1):
                S.append(S[j] + (3**cnt))
                i += 1




    print(S)

    return S[n-1]


print(solution(4))