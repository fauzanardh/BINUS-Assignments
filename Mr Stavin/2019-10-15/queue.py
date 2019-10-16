class Queue(object):
    def __init__(self, maxSize=5):
        self.maxSize = maxSize
        self.__queue = []

    def enqueue(self, data):
        if len(self.__queue) >= self.maxSize:
            raise Exception("Max Queue")
        self.__queue.append(data)
        return self

    def dequeue(self):
        return self.__queue.pop(0)

    def getQueue(self):
        return self.__queue[:]


class Stack(object):
    def __init__(self, maxSize=5):
        self.maxSize = maxSize
        self.__stack = []

    def push(self, data):
        if len(self.__stack) >= self.maxSize:
            raise Exception("Max Stacksize")
        self.__stack.insert(0, data)
        return self

    def pop(self):
        return self.__stack.pop(0)

    def getStack(self):
        return self.__stack[:]


q = Queue()
for x in range(0, 5):
    q.enqueue(x)
print(q.getQueue())
print(q.dequeue())
print(q.getQueue())

q = Stack()
for x in range(0, 5):
    q.push(x)
print(q.getStack())
print(q.pop())
print(q.getStack())
