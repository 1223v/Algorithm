def solution(n, t, m, timetable):
    answer = 0

    time_table = [int(timetable[i][:2]) * 60 + int(timetable[i][3:]) for i in range(len(timetable))]
    time_table.sort()

    bus_time = [9 * 60 + t * i for i in range(n)]

    i = 0
    for bt in bus_time:

        cnt = 0

        while cnt < m and i < len(time_table) and time_table[i] <= bt:
            cnt += 1
            i += 1

        if cnt < m:
            answer = bt


        else:

            answer = time_table[i - 1] - 1


    return str((answer // 60)).zfill(2) + ":" + str((answer % 60)).zfill(2)


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))