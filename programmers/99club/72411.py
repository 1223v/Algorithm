# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    graph = defaultdict(int)
    for i in orders:
        tmp = list(map(str,i))
        print(tmp)
        for k in course:
            if len(tmp) >= k:
                for com in combinations(tmp,k):
                    com_lst = list(com)
                    com_lst.sort()
                    graph[''.join(map(str,com_lst))] += 1

    lst_graph = list(graph.items())
    lst_graph.sort(key=lambda x:x[1])


    result = defaultdict(list)

    for s, num in lst_graph:
        result[len(s)].append((num,s))

    print(result)
    for i in course:
        if len(result[i]) < 1:
            continue

        result[i].sort(reverse=True)


        if result[i][0][0] <= 1:
            continue

        answer.append(result[i][0][1])

        for num in range(1,len(result[i])):

            if result[i][0][0] == result[i][num][0]:
                answer.append(result[i][num][1])
            else:
                break

    answer.sort()


    return answer

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

