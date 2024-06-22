
# def power(base=1, exp=0):
#     return base ** exp


position = '사원'
salary = 455700000
print(f"직급: {position} 연봉: {salary:,}원")




def Digit_sum(num, pos):
    digit = ['만', '천', '백', '십', '일']
    hap = 0
    # digit 이용 해당 위치 저장
    x = digit.index(pos)

    # 숫자를 문자열로 변환
    num_str = str(num)

    # 자리수를 맞추기 위해 앞에 0을 추가
    num_str = num_str.zfill(5)

    # x 위치부터 끝까지 합 구하기
    for a in num_str[x:]:
        hap += int(a)

    print('합', hap)



    def Pass(record):
        return record['점수'] >= 90 and record['전공'] == '컴퓨터'

    # 예제 data 리스트
    data = [
        {'아이디': 'user1', '점수': 85, '전공': '컴퓨터'},
        {'아이디': 'user2', '점수': 95, '전공': '컴퓨터'},
        {'아이디': 'user3', '점수': 90, '전공': '수학'},
        {'아이디': 'user4', '점수': 92, '전공': '컴퓨터'},
        {'아이디': 'user5', '점수': 88, '전공': '컴퓨터'},
    ]

    result = list(filter(Pass, data))
    print(result)

    result = list(filter(Pass,data))
    print(result)



Index = lambda word1, word2, idx: print((word1 if word1 > word2 else word2)[idx])

# 테스트
Index('ZOO', 'apple', 0)  # Z
Index('test', 'apple', 2) # s
Index('test', 'WORD', 2)  # R


t = (123, -45, 67)
result = set(map(lambda x: str(abs(x))[-1], t))
print(result)  # {'3', '5', '7'}

t = (-41, 456, 23, 141, -93)
result = set(map(lambda x: str(abs(x))[-1], t))
print(result)  # {'6', '3', '1'}


