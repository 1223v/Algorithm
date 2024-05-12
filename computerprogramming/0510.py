numbers = []

while True:
    try:
        num = float(input("1과 2 사이의 실수를 입력하세요: "))
        if 1 <= num <= 2:
            numbers.append(num)
        else:
            print("입력 범위를 벗어났습니다. 입력을 중단")
            break
    except ValueError:
        print("유효하지 않은 입력입니다. 실수를 입력해 주세요.")

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"입력된 실수의 평균은 {average:.2f} 입니다.")
else:
    print("유효한 입력이 없습니다.")