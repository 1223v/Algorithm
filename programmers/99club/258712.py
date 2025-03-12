from collections import defaultdict
from itertools import combinations
# 더 많은 선물을 준 사람이 받음
# 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면 선물 지수가 더 큰 사람이 받음
# 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않음
# 선물 지수 = 준 선물 - 받은 선물
def solution(friends, gifts):

    give_gift = defaultdict(list)
    take_gift = defaultdict(list)
    result = {}

    for i in friends:
        result[i] = 0

    for give_take in gifts:
        give, take= map(str,give_take.split())
        give_gift[give].append(take)
        take_gift[take].append(give)

    print(give_gift.items())
    print(take_gift.items())
    for i in combinations(friends,2):
        if i[1] in give_gift[i[0]] or i[0] in give_gift[i[1]]:
            if give_gift[i[0]].count(i[1]) > give_gift[i[1]].count(i[0]):
                print(i[0],i[1])
                result[i[0]] += 1

            elif give_gift[i[0]].count(i[1]) < give_gift[i[1]].count(i[0]):
                result[i[1]] += 1

            elif give_gift[i[0]].count(i[1]) == give_gift[i[1]].count(i[0]):

                if len(give_gift[i[0]]) - len(take_gift[i[0]]) > len(give_gift[i[1]]) - len(take_gift[i[1]]):
                    result[i[0]] += 1
                elif len(give_gift[i[0]]) - len(take_gift[i[0]]) < len(give_gift[i[1]]) - len(take_gift[i[1]]):
                    result[i[1]] += 1

        else:
            if len(give_gift[i[0]]) - len(take_gift[i[0]]) > len(give_gift[i[1]]) - len(take_gift[i[1]]):
                result[i[0]] += 1
            elif len(give_gift[i[0]]) - len(take_gift[i[0]]) < len(give_gift[i[1]]) - len(take_gift[i[1]]):
                result[i[1]] += 1

    answer = list(result.items())
    answer.sort(key=lambda x: x[1])



    return answer[-1][1]

print(solution(["muzi", "ryan", "frodo", "neo"],["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))