# s274 code fragment 7.12
# Code Fragment 7.12: A base class for managing a doubly linked list.
# nested class _Node
# header ve trailer (sentinel, kullanıcı görmüyor bunları)
# __len__ , is_empty , _insert_between(self,e,predecessor,successor) returns the new node,
# _delete_node(self,node) returns deleted element

class _DoublyLinkedBase():

    class _Node():

        __slots__ = '_element', '_prev', '_next'

        def __init__(self, e, prev, next):
            self._element = e
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, e, predecessor, successor):
        newnode = self._Node(e, predecessor, successor)
        predecessor._next = newnode
        successor._prev = newnode
        self.size += 1
        return newnode

    def _delete_node(self, node):
        p = node._prev
        n = node._next
        p._next = n
        n._prev = p
        self.size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element