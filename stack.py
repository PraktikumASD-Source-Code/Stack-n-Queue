class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.peek())  # Output: 3
print(s.pop())   # Output: 3
print(s.pop())   # Output: 2
print(s.size())  # Output: 1
