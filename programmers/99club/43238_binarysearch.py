def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n

    while start <= end:
        mid = int((start + end) / 2)
        result = 0
        for i in times:
            result += mid // i

            if result >= n:
                break

        if result >= n:
            answer = mid
            end = mid - 1

        else:
            start = mid + 1

    return answer
