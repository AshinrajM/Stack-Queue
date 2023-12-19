class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        NewNode = Node(value)
        self.top = NewNode
        self.height = 1

    def display(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        NewNode = Node(value)
        if self.top is None:
            self.top = NewNode
        else:
            self.top.next = NewNode
        self.height += 1

    def pop(self):
        if self.height is None:
            return None
        elif self.height == 1:
            return None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.height += 1
            return temp


    # Returns top element of stack
    def peek(self):
        if self.height:
            return self.top.value
        return None

    def is_empty(self):
        if self.top is None:
            return True
        return False


new=Stack(65)
new.push(857)
new.display()
new.pop()
new.display()