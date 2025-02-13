print("성적을 입력하세요.")

D_sungjuk = {}

def f1(korean, english, math):
    D_sungjuk["국어"] = korean
    D_sungjuk["영어"] = english
    D_sungjuk["수학"] = math
def f2():
    result = (D_sungjuk["국어"] + D_sungjuk["영어"] + D_sungjuk["수학"]) / 3
    return result
def f3(n):
    print("평균점수 : {:.2f}".format(n) )

while True:
    n = int(input("1) 점수입력 2) 점수수정 3) 종료 (0입력) :"))
    if n == 1:
        korean = int(input("국어점수는?"))
        english = int(input("영어점수는?"))
        math = int(input("수학점수는?"))
        f1(korean, english, math)



    elif n == 2:
        mod_subject = input("수정할 과목은?")
        if mod_subject == "국어":
            mod_score = int(input("몇 점으로 수정할까요?"))
            D_sungjuk["국어"] = mod_score

        elif mod_subject == "영어":
            mod_score = int(input("몇 점으로 수정할까요?"))
            D_sungjuk["영어"] = mod_score

        elif mod_subject == "수학":
            mod_score = int(input("몇 점으로 수정할까요?"))
            D_sungjuk["수학"] = mod_score
    elif n == 0:
        print("국어 :", D_sungjuk["국어"])
        print("영어 :", D_sungjuk["영어"])
        print("수학 :", D_sungjuk["수학"])
        total = f2()
        f3(total)
        break

    else:
        print("잘못 입력하셨습니다.")
