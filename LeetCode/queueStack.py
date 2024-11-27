from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

        while self.queue2:
            self.queue1.append(self.queue2.popleft())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue2.popleft() if not self.empty() else None

    def top(self) -> int:
        return self.queue2[0] if not self.empty() else None

    def empty(self) -> bool:
        return not self.queue2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()