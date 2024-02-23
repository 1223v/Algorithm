from collections import deque

# 입력: N은 리스트의 길이, K는 뒤집을 수 있는 부분 리스트의 길이
N,K=map(int,input().split())
# 리스트 L에 문자열 형태로 입력받은 숫자들을 저장
L=list(input().split())

# 방문한 상태를 저장할 집합, 초기 상태로 리스트 L의 문자열 형태를 저장
visitedS=set("".join(L))
# 탐색을 위한 큐 초기화, 시작 상태와 뒤집기 횟수(0) 포함
q=deque([["".join(L),0]])

# 최종 답을 저장할 변수, 초기값은 -1(불가능한 경우를 의미)
ans=-1
# BFS 탐색 시작
while(q):
    # 큐에서 현재 상태(word)와 뒤집기 횟수(cnt)를 가져옴
    word,cnt=q.popleft()
    # 현재 상태의 문자열을 리스트로 변환
    tempL=list(word)
    print(list(tempL))

    # 현재 상태가 오름차순으로 정렬된 경우, 탐색을 종료하고 cnt를 답으로 설정
    if tempL==sorted(tempL):
        ans=cnt
        break

    # 가능한 모든 위치에서 길이 K의 부분 리스트를 뒤집음
    for i in range(N-K+1):
        # 현재 상태를 복사하여 새로운 상태를 생성
        newL = list(tempL)
        # 뒤집을 대상 부분 리스트 선택
        targetL=newL[i:i+K]
        # 선택된 부분 리스트를 뒤집음
        targetL.reverse()
        # 뒤집은 결과를 원래 리스트에 반영
        for j in range(K):
            newL[i+j]=targetL[j]
        # 새로운 상태를 문자열로 변환
        newWord="".join(newL)
        # 새로운 상태가 이전에 방문하지 않은 상태인 경우, 방문 처리 후 큐에 추가
        if newWord not in visitedS:
            visitedS.add(newWord)
            q.append([newWord,cnt+1])

# 최소 뒤집기 횟수 출력
print(ans)
