import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)

# 4번 조건 : 색상 리스트 사용
colors = ["red", "green", "blue", "yellow", "purple", "cyan", "magenta", "orange"]


# 2번 조건 : 1개 이상의 함수를 포함
# 도형 그리기 함수
def draw(sides, length, color):

    # 주어진 변의 수, 변의 길이, 색상으로 도형을 그립니다.
    angle = 360 / sides  # 각 변 사이의 각도를 계산
    t.color(color)  # 터틀의 색상을 설정
    for _ in range(sides):  # 변의 수 만큼 반복
        t.forward(length)  # 변의 길이만큼 앞으로 이동
        t.right(angle)  # 계산된 각도만큼 오른쪽으로 회전


# 화면 채우기
def draw_shapes(num_shapes, min_sides=3, max_sides=10, min_length=10, max_length=100):
    # 1번 조건 : 중첩 반복문 사용
    for _ in range(num_shapes):  # 지정된 도형의 수 만큼 반복
        x = random.randint(-300, 300)  # x 좌표를 랜덤하게 선택
        y = random.randint(-300, 300)  # y 좌표를 랜덤하게 선택
        t.penup()  # 선을 그리지 않고 이동
        t.goto(x, y)  # 랜덤하게 선택된 좌표로 이동
        t.pendown()  # 선 그리기 시작

        nested_count = random.randint(2, 5)  # 중첩 도형의 수를 랜덤하게 설정
        for _ in range(nested_count):  # 중첩 도형의 수 만큼 반복

            # 3번 조건 : 랜덤모듈의 난수를 적용
            sides = random.randint(min_sides, max_sides)  # 변의 수를 랜덤하게 선택
            length = random.randint(min_length, max_length)  # 변의 길이를 랜덤하게 선택
            color = random.choice(colors)  # 색상을 랜덤하게 선택

            draw(sides, length, color)  # 도형을 그림
            t.right(360 / nested_count)  # 중첩 도형을 회전


# 2번 조건 : 키워드 인수 사용
def main(num_shapes, min_sides=3, max_sides=10, min_length=10, max_length=100):

    # 키워드 인수로 전달됩니다.
    draw_shapes(num_shapes, min_sides, max_sides, min_length, max_length)


# 4번 조건 : 딕셔너리 및 튜플 사용
# 딕셔너리를 사용한 키워드 인수
params = {
    "num_shapes": 10,  # 도형의 수
    "min_sides": 3,  # 최소 변의 수
    "max_sides": 8,  # 최대 변의 수
    "min_length": 20,  # 최소 변의 길이
    "max_length": 50  # 최대 변의 길이
}

# 도형의 수, 변의 수, 길이 등을 담은 튜플 리스트
shape_specs = [
    (params["num_shapes"], params["min_sides"], params["max_sides"], params["min_length"], params["max_length"])
]

# 4번 조건 : 딕셔너리 및 튜플 사용
for spec in shape_specs:
    main(*spec)  # 튜플을 키워드 인수로 전달하여 메인 함수 호출

turtle.done()
