def solution(routes):
    answer = 0

    routes.sort(key=lambda x:(x[1],x[0]))
    print(routes)
    cnt = 1

    top = routes[0][1]
    for i in range(1,len(routes)):
        if routes[i][0] <= top:
            continue



        else:
            cnt += 1
            top=routes[i][1]






    return cnt

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))