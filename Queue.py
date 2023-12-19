class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def display(self):
        if self.length:
            temp = self.first
            while temp:
                print(temp.value)
                temp = temp.next
        else:
            print("Queue is empty!")

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.length <= 1:
            self.first=self.last=None
            return None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -= 1
        return True
    
    def peek(self):
        if self.length:
            return self.top.value
        return None

    def is_empty(self):
        if self.first is None:
            return True
        return False


new_queue = MyQueue(69)
new_queue.enqueue(65)
new_queue.enqueue(45)
new_queue.enqueue(47)
new_queue.dequeue()
new_queue.display()
