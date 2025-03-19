from collections import defaultdict
from itertools import product
from bisect import bisect_left


def solution(info, query):
    graph = defaultdict(list)

    for i in info:
        lang, position, stack, menu, score = map(str, i.split())

        graph[lang + position + stack + menu].append(int(score))

    for key in graph.keys():
        graph[key].sort()
    result = [0] * (len(query))
    d = 0
    for q in query:
        s = list(map(str, q.split()))
        s = [i for i in s if i != 'and']

        tmp1, tmp2, tmp3, tmp4 = [], [], [], []

        if s[0] == '-':
            tmp1.append('cpp')
            tmp1.append('java')
            tmp1.append('python')

        else:
            tmp1.append(s[0])

        if s[1] == '-':
            tmp2.append('backend')
            tmp2.append('frontend')


        else:
            tmp2.append(s[1])

        if s[2] == '-':
            tmp3.append('junior')
            tmp3.append('senior')


        else:
            tmp3.append(s[2])

        if s[3] == '-':
            tmp4.append('chicken')
            tmp4.append('pizza')


        else:
            tmp4.append(s[3])

        k = list(product(tmp1, tmp2, tmp3, tmp4))

        for w in k:
            stmp = ''.join(map(str, w))

            left = bisect_left(graph[stmp], int(s[4]))

            result[d] += len(graph[stmp]) - left

        d += 1

    return result


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))