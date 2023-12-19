from collections import deque


class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1:
            self.q1.popleft()

    def top(self):
        if self.q1:
            return self.q1[0]
        return None

    def size(self):
        return len(self.q1)


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print("current size: ", s.size())
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())

print("current size: ", s.size())


# deque stands for "double-ended queue," and it is a data structure that allows
# elements to be added or removed from both ends with O(1) time complexity.
#  In Python, the collections module provides a built-in implementation of a deque through the deque class.
