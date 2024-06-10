#공백 없이 $가 중간에 한개 이상 포함된 문자열을 입력받고 $ 기준으로 각 문자열을 딕셔너리로 만드는 프로그램

#실행 예)
#입력 : test$2345$안녕$파이썬
#출력 : {0:'test', 1: '2345', 2: '안녕', 3:'파이썬' }


input_string = input("입력 : ").split('$')
output_dict = {i : input_string[i] for i in range(len(input_string))}
print("출력 :", output_dict)
