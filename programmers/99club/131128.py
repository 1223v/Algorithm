def solution(X,Y):

    result = []


    count_x = [0] * 10
    count_y = [0] * 10

    for i in range(len(X)):
        count_x[int(X[i])] += 1
    for i in range(len(Y)):
        count_y[int(Y[i])] += 1

    for i in range(9,-1,-1):
        common_count = min(count_x[i],count_y[i])
        if common_count > 0:
            result.extend([str(i)] * common_count)

    answer = ''.join(result)
    if not answer:  # 공통 숫자가 없는 경우
        return "-1"
    if answer == "0" * len(answer):  # 결과가 모두 0인 경우
        return "0"
    return answer


print(solution("100","203045"))
