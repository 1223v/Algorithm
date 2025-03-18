def solution(queue1, queue2):
    answer = -2

    total = (sum(queue1) + sum(queue2)) // 2

    queue_length = len(queue1) * 3
    q1 = sum(queue1)
    q2 = sum(queue2)
    total_queue1 = queue1 + queue2 + queue1
    total_queue2 = queue2 + queue1 + queue2
    one_start = 0
    two_start = 0
    cnt = 0
    while True:


        if q1 == total and q2 == total:

            break

        if queue_length < cnt:
            return -1


        if q1 < total and q2 > total:

            if two_start >= len(total_queue2):
                two_start %= len(total_queue2)

            q2 -= total_queue2[two_start]
            q1 += total_queue2[two_start]

            two_start += 1
            cnt += 1

        elif q2 < total and q1 > total:
            if one_start >= len(total_queue1):
                one_start %= len(total_queue1)

            q1 -= total_queue1[one_start]
            q2 += total_queue1[one_start]

            one_start += 1
            cnt += 1



    return cnt

print(solution(	[1, 1], [1, 5]))