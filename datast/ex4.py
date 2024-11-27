def counter(result):
    fiveh_coin, oneh_coin, fifty_coin, ten_coin = 0,0,0,0
    fiveh_coin += result // 500
    result = result % 500
    oneh_coin += result // 100
    result = result % 100
    fifty_coin += result // 50
    result = result % 50
    ten_coin += result // 10
    return fiveh_coin, oneh_coin, fifty_coin, ten_coin

total_point = 0
while True:
    money = int(input('투입한 돈 : '))
    if money == 0:
        print("감사합니다. 안녕히가세요.")
        break
    price = int(input("물건값 : "))

    result = money - price
    print(f"거스름돈 : \\{result}원")

    fiveh_coin, oneh_coin, fifty_coin, ten_coin = counter(result)

    if fiveh_coin + oneh_coin + fifty_coin+ten_coin > 5:
        ans = input('동전의 개수가 많습니다. 포인트로 적립해 드릴까요?(Y or N)').upper()
        if  ans == 'Y':
            total_point = result + total_point
            print(f"{result} 포인트가 적립되었습니다. 현재까지의 누적포인트 : {total_point}")
        else:
            print("500원 동전의 개수: ", fiveh_coin)
            print("100원 동전의 개수: ", oneh_coin)
            print("50원 동전의 개수: ", fifty_coin)
            print("10원 동전의 개수: ", ten_coin)

    else:
        print("500원 동전의 개수: ",fiveh_coin)
        print("100원 동전의 개수: ", oneh_coin)
        print("50원 동전의 개수: ",fifty_coin )
        print("10원 동전의 개수: ", ten_coin)


