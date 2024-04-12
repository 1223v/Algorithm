
x = int(input("x위치 : "))
y = int(input("y위치 : "))

if x > 0 and y>0:
    print("제 1분면에 위치한다")

elif x > 0 and y < 0:
    print("제 4분면에 위치한다")

elif x < 0 and y > 0:
    print("제 2분면에 위치한다")

elif x < 0 and y < 0:
    print("제 3분면에 위치한다")

else:
    print("기타위치")