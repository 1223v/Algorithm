import heapq


def solution(operations):


    max_hq = []
    min_hq = []

    for command in operations:

        cm, value = map(str,command.split())

        if cm == "I":
            heapq.heappush(max_hq, -int(value))
            heapq.heappush(min_hq, int(value))

        elif cm == "D" and max_hq:
            if value == "1":
                x = heapq.heappop(max_hq)
                min_hq.remove(-x)
                heapq.heapify(min_hq)
            else:
                x = heapq.heappop(min_hq)
                max_hq.remove(-x)
                heapq.heapify(max_hq)

    if max_hq and min_hq:
        return [-max_hq[0],min_hq[0]]

    else:

        return [0,0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))