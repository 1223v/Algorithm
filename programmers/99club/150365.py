# https://school.programmers.co.kr/learn/courses/30/lessons/150365

# r, l, d, u
import sys
sys.setrecursionlimit(10**5)
di,dj = [0,0,1,-1],[1,-1,0,0]
def solution(n, m, x, y, r, c, k):


    result = []

    min_value = abs(r-x) + abs(c-y)

    if min_value > k or (k-min_value) % 2 != 0:
        return "impossible"

    def dfs(tmp, ci,cj):
        if result:
            return
        if len(tmp) == k:

            if ci == r and cj == c:
                result.append(tmp)

            return

        for i in range(4):
            ni,nj = ci + di[i],cj + dj[i]
            if 1 <= ni < n+1 and 1 <= nj < m+1:
                if abs(ni-r) + abs(nj-c) + len(tmp) +1 <= k:
                    if i == 0:

                        dfs(tmp + 'r', ni, nj)
                    elif i == 1:

                        dfs(tmp + 'l', ni, nj)
                    elif i == 2:

                        dfs(tmp + 'd', ni, nj)
                    elif i == 3:
                        dfs(tmp + 'u', ni, nj)




    dfs("",x,y)



    return result[0] if result else "impossible"

print(solution(3,4,2,3,3,1,5))