def Digit_sum(num, pos):
    digit = ['만', '천', '백', '십', '일']
    hap = 0
    # digit 이용 해당 위치 저장
    x = digit.index(pos)



    # x 위치부터 끝까지 합 구하기
    for a in str(num)[len(str(num)) - len(digit) + x:]:
        hap += int(a)

    print('합', hap)

Digit_sum(345,'백')