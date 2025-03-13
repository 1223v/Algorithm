di,dj = [0,0,1,-1],[1,-1,0,0]

from collections import defaultdict

# 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용
#  두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용

def solution(numbers, hand):
    answer = ''
    graph = defaultdict(list)
    graph[1].append((0,0))
    graph[2].append((0, 1))
    graph[3].append((0, 2))
    graph[4].append((1, 0))
    graph[5].append((1, 1))
    graph[6].append((1, 2))
    graph[7].append((2, 0))
    graph[8].append((2, 1))
    graph[9].append((2, 2))
    graph['*'].append((3, 0))
    graph[0].append((3, 1))
    graph['#'].append((3, 2))

    now_L = [(3,0)]
    now_R = [(3,2)]



    for i in numbers:
        if i in [1,4,7]:

            now_L = graph[i]
            answer += 'L'


        elif i in [3,6,9]:
            now_R = graph[i]
            answer += 'R'

        else:

            now_R_to_i = abs(now_R[0][0] - graph[i][0][0]) + abs(now_R[0][1] - graph[i][0][1])
            now_L_to_i = abs(now_L[0][0] - graph[i][0][0]) + abs(now_L[0][1] - graph[i][0][1])
            if now_R_to_i > now_L_to_i:
                now_L = graph[i]
                answer += 'L'
            elif now_R_to_i < now_L_to_i:
                now_R = graph[i]
                answer += 'R'

            else:
                if hand == 'right':
                    now_R = graph[i]
                    answer += 'R'

                else:
                    now_L = graph[i]
                    answer += 'L'





    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))