class MinStack:

    def __init__(self):
        self.minStack = []
        self.min = float('inf')
        self.stack = []
        

    def push(self, value: int) -> None:
        if value < self.min:
            self.min = value

        self.stack.append(value)
        self.minStack.append(self.min)
        

    def pop(self) -> None:
        if not self.stack: return

        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.min = self.minStack[-1]
        else:
            self.min = float('inf')

        

    def top(self) -> int:
        if not self.stack: return
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()