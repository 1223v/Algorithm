# 다시 풀어볼 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/150367
# https://velog.io/@ggb05224/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C%ED%98%84-%EA%B0%80%EB%8A%A5%ED%95%9C-%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC-python
def dfs(b, i, depth):
    if depth == 0: # 리프 노드에 도달했다면
        return True # 포화 이진트리

    # 부모노드가 '0' 일때,
    # 왼쪽 자식 노드가 '1' 이거나 오른쪽 자식 노드가 '1' 이라면 포화 이진트리가 될 수 없음
    elif b[i] == '0':
        if b[i - depth] == '1' or b[i + depth] == '1':
            return False
    # 왼쪽 서브트리 탐색
    left = dfs(b, i - depth, depth // 2)
    # 오른쪽 서브트리 탐색
    right = dfs(b, i + depth, depth // 2)
    return left and right
def solution(numbers):
    answer = []
    for num in numbers: # num = 42
        b = bin(num)[2:] # b = 101010 / len(b) = 6
        nodes = bin(len(b) + 1)[2:] # nodes = 7 = 111

        # 포화 이진트리가 아닌 경우 더미 노드 0 추가
        if '1' in nodes[1:]:
            tmp = int('0b1' + '0' * len(nodes),2) - int('0b' + nodes, 2)
            b = '0' * tmp + b

        # 이미 포화 이진 트리 인경우
        result = dfs(b, len(b)//2, (len(b)+1)//4)
        answer.append(1 if result else 0)

    return answer