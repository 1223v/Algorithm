from collections import deque
from collections import defaultdict
def solution(record):
    answer = []
    queue = deque()
    graph = defaultdict(str)
    for s in record:

        tmp = list(map(str,s.split()))
        print(tmp)
        if len(tmp) == 2:
            entry, uuid = tmp[0],tmp[1]
        else:
            entry, uuid, name = tmp[0],tmp[1],tmp[2]
            graph[uuid] = name
        queue.append((uuid,entry))


    while queue:
        uuid, entry = queue.popleft()

        if entry == 'Enter':
            answer.append(graph[uuid]+"님이 들어왔습니다.")
        elif entry == 'Leave':

            answer.append(graph[uuid]+"님이 나갔습니다.")



    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))