class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity=capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0


    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear+1)%self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % self.capacity
            self.array[self.rear] = item

        else:
            pass

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

        else:
            pass

    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front+1 : self.rear+1])
        else:
            return str(self.array[self.front+1 : self.capacity]+ self.array[0:self.rear+1])

    def aaa(self):
        print("front = ", self.front)
        print("rear = ", self.rear)

# 원형큐 이해 필수 아래 상황에 따른 답
q = CircularQueue(8)
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.enqueue('D')
q.enqueue('E')
q.enqueue('F')
print(q)
q.aaa()
print(q.dequeue())
q.enqueue('G')
q.enqueue('H')
print(q)
print(q.dequeue())
q.enqueue('I')
print(q)

