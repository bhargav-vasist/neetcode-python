class MinStack:
    stck = []

    def __init__(self):
        stck = []

    def push(self, val: int) -> None:
        self.stck.append(val)

    def pop(self) -> None:
        self.stck.pop()

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return min(self.stck)


obj = MinStack()
obj.push(-1)
print(obj.top())
print(obj.getMin())
