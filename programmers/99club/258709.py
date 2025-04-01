from collections import defaultdict
from itertools import combinations, product
from bisect import bisect_left


def solution(dice):
    answer = []
    N = len(dice)
    dice_choice = [i for i in range(N)]

    dice_dict = defaultdict(list)

    A_tmp = combinations(dice_choice, N // 2)
    for lst in A_tmp:

        B_tmp = []
        for i in range(N):
            if i not in lst:
                B_tmp.append(i)

        A_lst = [dice[i] for i in lst]
        B_lst = [dice[i] for i in B_tmp]


        A_score = [sum(i) for i in product(*A_lst)]
        B_score = sorted([sum(i) for i in product(*B_lst)])

        wins = sum(bisect_left(B_score,i) for i in A_score)

        dice_dict[wins].extend(lst)



    max_value = max(dice_dict.keys())


    return [i+1 for i in dice_dict[max_value]]


print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))