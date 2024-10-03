from collections import defaultdict


def solution(friends, gifts):
    # 받은 내역
    gift_to = defaultdict(list)
    # 보낸 내역
    gift_from = defaultdict(list)
    # 결과
    result = {}
    # 방문 처리
    visited_friends = defaultdict(list)

    for i in friends:
        result[i] = 0

    for i in gifts:
        i_from, i_to = map(str, i.split())
        gift_from[i_from].append(i_to)
        gift_to[i_to].append(i_from)

    for i in friends:
        for j in friends:
            if i != j and j not in visited_friends[i]:
                if j in gift_from[i] or i in gift_from[j]:
                    if gift_from[i].count(j) > gift_from[j].count(i):
                        result[i] += 1
                    elif gift_from[i].count(j) < gift_from[j].count(i):
                        result[j] += 1
                    else:
                        if len(gift_from[i]) - len(gift_to[i]) < len(gift_from[j]) - len(gift_to[j]):
                            result[j] += 1
                        elif len(gift_from[i]) - len(gift_to[i]) > len(gift_from[j]) - len(gift_to[j]):
                            result[i] += 1

                else:
                    if len(gift_from[i]) - len(gift_to[i]) < len(gift_from[j]) - len(gift_to[j]):
                        result[j] += 1
                    elif len(gift_from[i]) - len(gift_to[i]) > len(gift_from[j]) - len(gift_to[j]):
                        result[i] += 1
                visited_friends[i].append(j)
                visited_friends[j].append(i)

    return max(result.values())