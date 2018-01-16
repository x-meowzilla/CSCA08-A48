class StringQueue():

    SEPARATOR = ','

    def __init__(self):
        self._container = ""

    def __str__(self):
        return self._container

    def enqueue(self, obj):
        self._container += str(obj) + self.SEPARATOR

    def dequeue(self):
        # find the first separator, then slice to separate the object from
        # container, lastly update the container and return object
        i = self._container.find(self.SEPARATOR)
        obj = self._container[:i]
        self._container = self._container[i + 1:]
        return obj

    def is_empty(self):
        return self._container == ""

if __name__ == "__main__":
    q = StringQueue()
    print(q)

    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    print(q)

    a = q.dequeue()
    print("dequeue", a)
    b = q.dequeue()
    print("dequeue", b)
    print(q)

    q.dequeue()
    q.dequeue()
    print(q)
    print(q.is_empty())
