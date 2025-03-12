import math
def solution(fees, records):
    answer = []
    graph = {}
    record = {}

    for i in records:
        time, num, inout = map(str, i.split())


        if num not in graph and inout == 'IN':
            if num not in record:
                record[num] = 0
            graph[num] = time

        elif num in graph and inout == 'OUT':

            in_hour,in_min = map(int,graph.pop(num).split(":"))
            out_hour, out_min = map(int, time.split(":"))
            record[num] += (out_hour * 60 + out_min) - (in_hour* 60 + in_min)

    if len(list(graph.items())) > 0:
        for num, time in list(graph.items()):
            in_hour, in_min = map(int, time.split(":"))
            record[num] += (23*60 + 59) - (in_hour*60 + in_min)

    result = []
    print(record.items())
    for num, time in list(record.items()):
        if time > fees[0]:
            result.append((num,fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]))
        else:
            result.append((num,fees[1]))

    result.sort(key=lambda x: x[0])
    for i,j in result:
        answer.append(j)
    return answer

print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))