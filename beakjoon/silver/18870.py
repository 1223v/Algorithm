import sys
input = sys.stdin.readline

# 정렬 후, dict 테이블을 만들어 탐색
n = int(input())

numbers = list(map(int,input().split()))
numset = set(numbers) # 매핑을 위한 중복 제거

a = list(numset)
a.sort() # 매핑을 위한 정렬

numdict = {}

for i in range(len(a)): # 매핑
    numdict[a[i]] = i # 정렬된 첫번째 값을 0번으로 지정 -10 : 0 이런식으로 매핑

for i in numbers: # 기존의 배열을 돌면서 해당 값을 탐색
    print(numdict[i], end=' ')