# 두 사람이 선물을 주고받은 기록이 있다면,
#       더 많은 선물을 준 사람이 다음 달에 선물을 하나 받음
# 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면,
#       선물 지수가 더 큰 사람이 선물 지수가 선물을 하나 받음
#       만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않음.

# 예를 들어 A가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 A의 선물 지수는 -7
#
from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    answer = 0

    gift_to_lst = defaultdict(list) # 받은
    gift_from_lst = defaultdict(list) # 준

    for s in gifts:
        from_p, to_p =  map(str,s.split())
        gift_to_lst[to_p].append(from_p)
        gift_from_lst[from_p].append(to_p)

    score = defaultdict(int)
    for i,j in combinations(friends,2):

        # 두 사람이 선물을 주고받은 기록이 있다면,
        if j in gift_from_lst[i] or i in gift_from_lst[j]:
            give_i = gift_from_lst[i].count(j)
            give_j = gift_from_lst[j].count(i)
            if give_i > give_j:
                score[i] += 1
            elif give_i < give_j:
                score[j] += 1
            # 주고받은 수가 같다면,
            else:
                #선물 지수가 더 큰 사람이 선물 지수가 선물을 하나 받음
                i_score = len(gift_from_lst[i]) - len(gift_to_lst[i])
                j_score = len(gift_from_lst[j]) - len(gift_to_lst[j])
                #만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않음.
                if i_score > j_score:
                    score[i] += 1
                elif i_score < j_score:
                    score[j] += 1

        # 두 사람이 선물을 주고받은 기록이 하나도 없다면,
        else:
            # 선물 지수가 더 큰 사람이 선물 지수가 선물을 하나 받음
            i_score = len(gift_from_lst[i]) - len(gift_to_lst[i])
            j_score = len(gift_from_lst[j]) - len(gift_to_lst[j])
            # 만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않음.
            if i_score > j_score:
                score[i] += 1
            elif i_score < j_score:
                score[j] += 1


    if len(score.values())<=0:
        return 0
    max_value = max(score.values())
    return max_value


print(solution(["a", "b", "c"],["a b", "b a", "c a", "a c", "a c", "c a"]))
