from itertools import combinations,product
from bisect import bisect_left
from collections import defaultdict
def solution(dice):
    result = []
    N = len(dice)
    # A가 먼저 n / 2개의 주사위를 가져가면
    # B가 남은 n / 2개의 주사위를 가져감

    #  각각 가져간 주사위를 모두 굴린 뒤, 나온 수들을 모두 합해 점수를 계산

    # 점수가 더 큰 쪽이 승리하며, 점수가 같다면 무승부

    # A는 자신이 승리할 확률이 가장 높아지도록 주사위를 가져가려 함
    dices = [i for i in range(N)]
    max_value = defaultdict(list)
    def chk(A_tmp):
        B_tmp = []
        for i in dices:
            if i not in A_tmp:
                B_tmp.append(i)

        print(A_tmp,B_tmp)
        A = [dice[i] for i in A_tmp]
        B = [dice[i] for i in B_tmp]

        A_nums = [sum(i) for i in product(*A)]
        B_num = sorted([sum(i) for i in product(*B)])

        wins = sum(bisect_left(B_num,num) for num in A_nums)
        max_value[wins].extend(A_tmp)




    for lst in combinations(dices,N//2):
        chk(lst)

    print(max_value)
    print(max(max_value.keys()))
    print([x + 1 for x in max_value[max(max_value.keys())]])



    return result

print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))