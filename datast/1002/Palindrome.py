def check(s):

    stack = []
    s = ''.join(filter(str.isalnum, s)).lower()
    length = len(s)

    for i in range(length // 2):
        stack.append(s[i])
    start = (length // 2) if length % 2 == 0 else (length // 2) + 1

    for i in range(start, length):
        if s[i] != stack.pop():
            return False
    return True



tests = [
    "A man, a plan, a canal, Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon"
]

for string in tests:
    result = "회문" if check(string) else "회문 아님"
    print(f"'{string}' => {result}")
