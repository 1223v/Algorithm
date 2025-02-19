import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    s = input().rstrip()
    start = 0
    end = len(s) - 1


    while start <= end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            # 오른쪽 문자 제거 후 회문 검사
            temp1 = s[:end] + s[end+1:]
            # 왼쪽 문자 제거 후 회문 검사
            temp2 = s[:start] + s[start+1:]

            if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
                print(1)  # 유사회문인 경우
                break
            else:
                print(2)  # 회문도, 유사회문도 아닌 경우
                break
    else:
        print(0)  # 회문인 경우
