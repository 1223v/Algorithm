import sys
import math
input = sys.stdin.readline

# 1,2,3,4 => 1
# 1,2,7,6,4 =>4
A = list(map(int,input().split()))
visited = [False] * (len(A)+1)
result = []
check = False
def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            #print("isPrime 확인", x)
            return False
    return True


def dfs(u,v,depth):
    global result, check
    if not check:
        check=True
        #print("체크썸", A[v])

    if depth == 3:
        if isPrime(u):
            print(u)
            result.append(u)

        return
    else:
        visited[v] = True
        for i in range(v,len(A)):
            if not visited[i]:
                dfs(u+A[i],i, depth+1)
        visited[v] = True

for i in range(len(A)):
    dfs(A[i],i,1)
    visited = [False] * (len(A)+1)
    check = False


print(len(result))
