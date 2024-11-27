class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
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
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
        else:
            print("리스트 overflow 또는 유효하지 않은 위치임")

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1
            return e
        else:
            print("리스트 underflow 또는 유효하지 않은 위치임!")

    def replace(self, pos, e):
        if 0 <= pos < self.size:
            old_value = self.array[pos]
            self.array[pos] = e
            return old_value  # 교체된 이전 값을 반환할 수 있음
        else:
            print("유효하지 않은 위치임!")
            return None

    def __str__(self):
        return str(self.array[0:self.size])


# 테스트 코드
L = ArrayList(50)

if __name__ == "__main__":
    print("최초 ", L)
    L.insert(0, 10)
    L.insert(1, 20)
    L.insert(2, 30)
    L.insert(3, 40)
    print(L)

    # Replace 연산 테스트
    old_value = L.replace(2, 50)
    print(f"교체된 값: {old_value}")
    print("교체 후: ", L)

    L.replace(0, 100)
    print("0번째 요소 교체 후: ", L)
