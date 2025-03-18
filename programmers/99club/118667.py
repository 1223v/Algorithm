# 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
# 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천
# 아이디의 길이는 3자 이상 15자 이하
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용
# 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없음

# 1 : new_id의 모든 대문자를 -> 소문자로 치환
# 2 : new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
# 3 : new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
# 4 : new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
# 5 : new_id가 빈 문자열이라면, new_id에 "a"를 대입
# 6 : new_id의 길이가 16자 이상 -> new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
#       만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
# 7 : new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임

def sol1(s):

    return s.lower()

def sol2(s):
    s = s.replace("~","")
    s = s.replace("!", "")
    s = s.replace("@", "")
    s = s.replace("#", "")
    s = s.replace("$", "")
    s = s.replace("%", "")
    s = s.replace("^", "")
    s = s.replace("&", "")
    s = s.replace("*", "")
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("=", "")
    s = s.replace("+", "")
    s = s.replace("[", "")
    s = s.replace("{", "")
    s = s.replace("]", "")
    s = s.replace("}", "")
    s = s.replace(":", "")
    s = s.replace("?", "")
    s = s.replace(",", "")
    s = s.replace("<", "")
    s = s.replace(">", "")
    s = s.replace("/", "")

    return s

def sol3(s):

    while ".." in s:
        s = s.replace("..",".")


    return s

def sol4(s):
    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    if s[0] == "." and s[-1] == '.':
        return s[1:-1]

    if s[0] == ".":
        return s[1:]

    if s[-1] == '.':
        return s[:-1]

    return s

def sol5(s):
    # 5 : new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if len(s) == 0:
        s = "a"
    return s

def sol6(s):
    # 6 : new_id의 길이가 16자 이상 -> new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    #       만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거

    if len(s) >= 16:

        tmp = s[:15]
        if tmp[-1] == '.':
            return tmp[:-1]

        return tmp

    else:

        return s



def sol7(s):
    # 7 : new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임

    tmp=s[-1]
    while len(s) <= 2:
        s += tmp

    return s



def solution(new_id):
    answer = 's'


    return sol7(sol6(sol5(sol4(sol3(sol2(sol1(new_id)))))))

print(solution("...!@BaT#*..y.abcdefghijklm"))