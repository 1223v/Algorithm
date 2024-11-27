def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def change(s):
    stack = []

    for char in s:
        # 피연산자일 경우 스택에 넣는다
        if char.isalnum():  # 알파벳이나 숫자라면
            stack.append(char)
        # 연산자일 경우 스택에서 두 개의 피연산자를 꺼내고 괄호로 감싸서 다시 스택에 넣는다
        elif char.strip():  # 공백이 아닌 경우에만 연산자 처리
            x = stack.pop()
            y = stack.pop()

            # 스택에서 꺼낸 두 피연산자의 우선순위를 비교하여 괄호를 조정
            if len(stack) > 0 and precedence(char) < precedence(stack[-1]):
                stack.append(f'({y}{char}{x})')
            else:
                stack.append(f'{y}{char}{x}')

    # 결과는 스택에 남은 하나의 문자열이 된다
    return stack[-1]


# 후위 표기식을 중위 표기식으로 변환
tests = [
    'ABC-D*+',
    'AB+CD-/E+',
    'ABCDE*+/+',
    'XYZ+AB-* -',
    'AB+C-DE*+'
]

results = {postfix: change(postfix) for postfix in tests}

for postfix, infix in results.items():
    print(f"{postfix} => {infix}")
