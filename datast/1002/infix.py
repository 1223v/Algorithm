# 연산자 우선순위를 정의하는 함수
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '(':
        return 0
    return -1

# 주어진 중위 표기식을 후위 표기식으로 변환하는 함수
def change(expression):
    # 출력 결과를 저장할 리스트
    result = []
    # 연산자를 저장할 스택
    stack = []

    for char in expression:
        # 피연산자일 경우 결과 리스트에 추가
        if char.isalnum():  # 알파벳이나 숫자라면
            result.append(char)

        # '('는 무조건 스택에 넣는다
        elif char == '(':
            stack.append(char)

        # ')'를 만나면 '('까지 스택에서 팝하여 결과에 추가
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # '('를 스택에서 제거

        # 연산자일 경우
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(char)

    # 남은 연산자들을 결과에 추가
    while stack:
        result.append(stack.pop())

    # 리스트를 문자열로 변환하여 반환
    return ''.join(result)


# 테스트
tests = [
    "(A/B)*C",
    "A + (B*C)-D/E",
    "(X+Y)-(W*Z)/V",
    "U*V*W+X-Y",
    "A/B*C-D+E",
    "A*(B+C)/D-E"
]

for exp in tests:
    print(f"{exp} => {change(exp)}")
