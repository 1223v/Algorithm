# 빈 테이블(O)을 의미
# 응시자가 앉아있는 자리(P)를 의미
# 파티션(X)을 의미
di,dj = [0,0,1,-1], [1,-1,0,0]
def solution(places):
    answer = []

    def dfs(n,graph,ci,cj,visited):
        if n == 2:
            return

        visited[ci][cj] = True
        for i in range(4):
            ni,nj = ci + di[i], cj+dj[i]
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                if graph[ni][nj] == "O":
                    if dfs(n+1,graph,ni,nj,visited):
                        return True

                elif graph[ni][nj] == "P":
                    return True

    for place in places:
        tmp = []
        for i in place:
            s = list(map(str,i))
            tmp.append(s)

        chk = False
        print(tmp)
        for i in range(5):
            for j in range(5):
                if tmp[i][j] == 'P':
                    visited = [[False] * 5 for _ in range(5)]
                    if dfs(0, tmp,i,j,visited):
                        answer.append(0)
                        chk = True
                        break
            if chk:
                break
        else:
            answer.append(1)






    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))