# https://school.programmers.co.kr/learn/courses/30/lessons/60060?language=python3


def solution(words, queries):
    answer =[]
    data = [[] for _ in range(10001)]
    redata = [[] for _ in range(10001)]

    def bisect_left(a, target):
        start,end = 0, len(a)
        while start < end:
            mid = (start + end) // 2

            if a[mid] < target:
                start = mid + 1

            else:
                end = mid
        return start

    def bisect_right(a, target):
        start, end = 0, len(a)
        while start < end:
            mid = (start + end) // 2

            if a[mid] < target:
                start = mid + 1

            else:
                end = mid
        return end

    def count(a, left_value, right_value):
        left_index = bisect_left(a,left_value)
        right_index = bisect_right(a,right_value)
        return right_index - left_index

    for i in words:
        data[len(i)].append(i)
        redata[len(i)].append(i[::-1])

    for i in range(10001):
        data[i].sort()
        redata[i].sort()

    for i in queries:
        if i[0] != "?":
            res = count(data[len(i)], i.replace("?", "a"), i.replace("?", "z"))
        else:
            res = count(redata[len(i)], i[::-1].replace("?","a"), i[::-1].replace("?","z"))

        answer.append(res)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))