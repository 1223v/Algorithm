from collections import Counter


def solution(s):
    answer = []
    s = s.replace("},{", " ")
    s = s.replace("{", "")
    s = s.replace("}", "")

    s = list(map(str, s.split()))

    res = []
    for i in s:
        tmp = list(map(int, i.split(',')))
        res += tmp

    result = []

    re1 = Counter(res).most_common()

    for i, j in re1:
        result.append(i)

    return result