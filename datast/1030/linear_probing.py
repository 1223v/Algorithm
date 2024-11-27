M = 13
table = [None] * M

def hashFn(key):
    return key % M

def insert(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] is None or table[i] == -1:  # 빈 슬롯에 삽입
            table[i] = key
            return
        i = (i + 1) % M  # 충돌이 발생하면 다음 위치로 이동
        count -= 1

def search(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] is None:  # 키가 없는 경우
            return None
        if table[i] == key:  # 키를 찾은 경우
            return table[i]
        i = (i + 1) % M  # 충돌 해결
        count -= 1
    return None  # 키를 찾지 못한 경우

def delete(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] is None:  # 키가 없는 경우
            return
        if table[i] == key:  # 키를 찾은 경우 삭제
            table[i] = -1
            return
        i = (i + 1) % M  # 충돌 해결
        count -= 1

data = [45, 27, 88, 9, 71, 60, 46, 38, 24]

for d in data:
    print("h(%2d) = %2d" % (d, hashFn(d)), end=' ')
    insert(d)
    print(table)

print("46 탐색 -->", search(46))
print("39 탐색 -->", search(39))
print("60 삭제 -->", end='')
delete(60)
print(table)
