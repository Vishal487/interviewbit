class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minimum) == 0:
            self.minimum.append(x)
        else:   
            self.minimum.append(min(self.minimum[-1], x))

    # @return nothing
    def pop(self):
        if len(self.stack) == 0:
            pass
        else:
            self.stack.pop()
            self.minimum.pop()


    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.minimum[-1]

s = MinStack()
s.push(10)
s.push(9)
print(s.getMin())
s.push(8)
print(s.getMin())
s.push(7)
print(s.getMin())
s.push(6)
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())

# correct answer for above input : 9 8 7 6 7 8 9 10 -1
"""
10 9 8 7
9 8 7 6 7
"""