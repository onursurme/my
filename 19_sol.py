class Empty(Exception):
    pass

# FIFO queue yaz, arka planda list kullansın
# list'i circular olarak kullansın
# _size ve _front (_front değişkeni queue'un en önündeki değerin data isimli list'teki indeksi)
# __init__ , __len__ , is_empty , first , dequeue , enqueue , _resize , __repr__

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            return Empty("the queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("the queue is empty")
        answer=self.first()
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        self._data[(self._front + self._size)%len(self._data)]=e
        self._size +=1

    def _resize(self, cap):                  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        newdata=[None]*cap
        for x in range(self._size):
            newdata[x] = self._data[(self._front + x)%len(self._data)]
        self._data = newdata
        self._front = 0

    def __repr__(self):    # bu metodu ben ekledim. __repr__ öneriliyor aslında
        return '['+','.join([self._data[(self._front+i) % len(self._data)] for i in range(self._size)])+']'

q1 = ArrayQueue()
q1.enqueue('a')
q1.enqueue('b')
print("q1=", q1)
print("len =", len(q1), "len data=", len(q1._data))
print("first =", q1.first())
print("is empty =", q1.is_empty())
print("dequeue =", q1.dequeue())
print("q1=", q1)
print("len =", len(q1), "len data=", len(q1._data))
print("first =", q1.first())
print("is empty =", q1.is_empty())
print("dequeue =", q1.dequeue())
print("q1=", q1)
print("len =", len(q1), "len data=", len(q1._data))
print("is empty=", q1.is_empty())
q1.enqueue('a')
q1.enqueue('b')
q1.enqueue('c')
q1.enqueue('d')
q1.enqueue('e')
q1.enqueue('f')
q1.enqueue('g')
q1.enqueue('h')
q1.enqueue('i')
q1.enqueue('j')
q1.enqueue('k')
q1.enqueue('l')
print("q1=", q1)
print("len =", len(q1), "len data=", len(q1._data))
print("first =", q1.first())
print("is empty =", q1.is_empty())
print("dequeue =", q1.dequeue())
print("dequeue =", q1.dequeue())
print("dequeue =", q1.dequeue())
print("dequeue =", q1.dequeue())
print("dequeue =", q1.dequeue())
print("dequeue =", q1.dequeue())
print("q1=", q1)
print("len =", len(q1), "len data=", len(q1._data))
print("dequeue =", q1.dequeue())
print("dequeue =", q1.dequeue())
print("dequeue =", q1.dequeue())
print("dequeue =", q1.dequeue())
print("q1=", q1)
print("len =", len(q1), "len data=", len(q1._data))
q1.enqueue('m')
q1.enqueue('n')
q1.enqueue('o')
q1.enqueue('p')
q1.enqueue('q')
print("q1=", q1)
print("len =", len(q1), "len data=", len(q1._data))
print("first =", q1.first())
print("is empty =", q1.is_empty())
print("enqueue =", q1.enqueue('r'))
print("enqueue =", q1.enqueue('s'))
print("q1=", q1)
print("len =", len(q1), "len data=", len(q1._data))
print("is empty=", q1.is_empty())
for x in range(10):
    q1.dequeue()
# print("first =",q1.first())  hata verir
