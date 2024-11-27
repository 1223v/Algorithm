class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

M = 13
table = [None] * M

def hashFn(key):
    return key % M

def insert(key):
    k = hashFn(key)
    n = Node(key)
    n.link = table[k]
    table[k] = n

def search(key):
    k = hashFn(key)
    n = table[k]
    while n is not None:
        if n.data == key:
            return n.data
        n = n.link
    return None

def delete(key):
    k = hashFn(key)
    n = table[k]
    before = None
    while n is not None:
        if n.data == key:
            if before is None:
                table[k] = n.link
            else:
                before.link = n.link
            return
        before = n
        n = n.link

def printTable():
    for i in range(M):
        n = table[i]
        if n is not None:
            print("[%2d] " % i, end='')
            while n is not None:
                print(n.data, end=' ')
                n = n.link
            print()

# 테스트
data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
for d in data:
    insert(d)

printTable()
print("46 탐색 -->", search(46))
print("39 탐색 -->", search(39))
print("60 삭제 -->", end='')
delete(60)
printTable()
