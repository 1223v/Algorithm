# 중첩반복, 리스트값 꺼내기, 인덱싱, 메서드 활용, %연산 활용 등을 알아보는 예제

# 단, turtle모듈은 중간 시험범위제외

import turtle

import random

t = turtle.Turtle()  # 파일안에 이름.메서드() = 함수

s = turtle.Turtle()

t.shape('turtle')

s.shape('turtle')

# 144도만큼 오른쪽 회전 하면서 100픽셀 5개 선 그리기

# for중첩

t.speed(0)

s.speed(9)

color = ["red", "yellow", "orange", "green", "navy", "purple"]

for a in range(50):  # 0 1 2 3 4 5 6(0).... 19 바깥쪽

    t.color(color[a % 6])  # %   0 - 5  거북이색, 선색

    t.penup()

    t.goto(random.randint(-300, 300), random.randint(-300, 300))

    t.pendown()

    t.begin_fill()

    s.color(color[a % 6])  # %   0 - 5  거북이색, 선색

    s.penup()

    s.goto(random.randint(-300, 300), random.randint(-300, 300))

    s.pendown()

    s.begin_fill()

    for i in range(5):  # 0 1 2 3 4

        t.fd(50)

        t.rt(144)

        s.fd(30)

        s.rt(144)

    t.end_fill()

    s.end_fill()

# 실수 또는 정수 들의 합출력

x = ["test", 34, 5.6, 'aaa', [3, 4, "tt"], [45, 67.8888, 4, 5, 6.7], "gg"]

hap = 0

for a in x:

    if type(a) == int or type(a) == float:

        hap += a

    elif type(a) == list:  # [3, 4 , "tt"]

        for b in a:  # 3 , 4 , "tt"

            if type(b) == int or type(b) == float:
                hap += b

            # 함수 모듈

print(round(hap, 2))