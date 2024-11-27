# 201921372 조현식
class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity  # capacity를 입력받은 값으로 설정해야 함
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            # 요소를 삽입할 공간을 만들기 위해 뒤로 한 칸씩 밀기
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            # 새로운 요소 삽입
            self.array[pos] = e
            self.size += 1
        else:
            print("리스트 overflow 또는 유효하지 않은 위치임")

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None  # 마지막 요소를 None으로 설정
            self.size -= 1
            return e
        else:
            print("리스트 underflow 또는 유효하지 않은 위치임!")

    def __str__(self):
        return str(self.array[0:self.size])

L = ArrayList(50)

if __name__ == "__main__":
    print("최초 ", L)
    L.insert(pos=0, e=10)
    L.insert(pos=0, e=20)
    L.insert(L.size, e=40)
    L.insert(pos=2, e=50)
    print(L)
    L.delete(2)
    print(L)
    L.delete(L.size - 1)
    print(L)
    L.delete(0)
    print(L)

