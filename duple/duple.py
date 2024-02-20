from collections import defaultdict  # defaultdict를 사용하기 위해 collections 모듈에서 import합니다.

def solution(s):
    # 입력된 문자열 s에서 가장 바깥쪽의 중괄호를 제거하고, 각 튜플을 '}' 문자로 분리합니다.
    subarr = s[1:len(s)-1].split('}')
    # 첫 번째 튜플에서 시작 부분의 '{' 문자를 제거합니다.
    subarr[0] = subarr[0][1:]
    # 두 번째 튜플부터는 앞에 붙은 ",{" 문자열을 제거합니다. 이 과정은 각 튜플을 분리하는 과정입니다.
    for i in range(1, len(subarr)):
        subarr[i] = subarr[i][2:]
    # 이제 각 튜플을 구성하는 숫자들을 쉼표(',')로 분리하여 리스트로 만듭니다.
    for i in range(len(subarr)):
        subarr[i] = subarr[i].split(',')

    # defaultdict를 사용하여 각 숫자가 몇 번 등장하는지 카운트합니다. 이 때, int로 초기화하여 0부터 카운트합니다.
    dic = defaultdict(int)
    # 분리된 각 튜플(sub)에 대하여 순회합니다.
    for sub in subarr:
        # 튜플을 구성하는 각 멤버(숫자)에 대하여 순회합니다.
        for member in sub:
            # 멤버가 빈 문자열이 아닐 때만 처리합니다. 이는 분리 과정에서 빈 문자열이 발생할 수 있기 때문입니다.
            if member:
                # 해당 숫자(member)의 카운트를 1 증가시킵니다.
                dic[member] += 1

    # 카운트된 결과를 바탕으로 (숫자, 등장 횟수) 형태의 튜플 리스트를 만듭니다.
    temp = []
    for key in dic.keys():
        temp.append((key, dic[key]))
    # 이 튜플 리스트를 등장 횟수에 따라 내림차순으로 정렬합니다. 등장 횟수가 많을수록 튜플의 앞쪽에 위치해야 합니다.
    temp.sort(key=lambda x:x[1], reverse=True)

    # 중간 결과 확인을 위해 subarr를 출력합니다. (이 부분은 실제 로직에는 필요하지 않으나, 코드의 동작을 이해하는 데 도움이 됩니다.)
    print(subarr)

    # 최종 결과를 저장할 리스트입니다.
    answer = []
    # 정렬된 temp 리스트에서 숫자 부분만 추출하여 정수로 변환 후 answer 리스트에 추가합니다.
    for i in range(len(temp)):
        answer.append(int(temp[i][0]))

    # 최종적으로 순서가 정렬된 숫자 리스트를 반환합니다.
    return answer

# 함수를 테스트하기 위한 입력 문자열입니다.
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# 함수를 실행하여 결과를 answer 변수에 저장합니다.
answer = solution(s)
# 최종 결과를 출력합니다.
print(answer)
