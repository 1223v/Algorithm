class ArraySet:

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def isFull(self):
        return self.size == self.capacity

    def __str__(self):
        return str(self.array[0:self.size])

    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.array[self.size - 1] = None  # 마지막 요소를 None으로 설정
                self.size -= 1
                return

    def union(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC

    def intersect(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    def __eq__(self, other):
        if self.size != other.size:
            return False
        for i in range(self.size):
            if not other.contains(self.array[i]):
                return False
        return True

# 테스트 코드
setA = ArraySet()
setA.insert("휴대폰")
setA.insert("지갑")
setA.insert("손수건")
print("set A:", setA)


setB = ArraySet()
setB.insert("빗")
setB.insert("파이썬 자료구조")
setB.insert("야구공")
setB.insert("지갑")
print("set B:", setB)

setA.delete("손수건")
setA.delete("발수건")
print("set A: ",setA)

setB.insert("빗")
print("set B: ",setB)

print('A ∪ B', setA.union(setB))
print('A ∪ B', setA.intersect(setB))
print('A - B', setA.difference(setB))
# 두 집합이 같은지 비교
print("set A == set B:", setA == setB)

setC = ArraySet()
setC.insert("휴대폰")
setC.insert("지갑")
print("set A: ",setA)
print("set C:", setC)

# 다른 집합과 비교
print("set A == set C:", setA == setC)