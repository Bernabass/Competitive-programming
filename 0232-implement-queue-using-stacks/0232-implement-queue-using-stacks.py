class MyQueue:

    def __init__(self):
        self.queue = []
        self.val = None
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.queue.reverse()
        popped = self.queue.pop()
        self.queue.reverse()
        return popped

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return self.queue == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
