class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def EnQueue(self, i):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s2.append(i)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def DeQueue(self):
        if len(self.s1) == 0:
            return -1
        i = self.s1[-1]
        self.s1.pop()
        return i
    
a=Queue()
a.EnQueue(56)
a.EnQueue(53)
a.EnQueue(543)
a.EnQueue(565)
print(a.DeQueue())



# Here Operation of Queue is executed by using 2 stacks.
