# Code Fragment 7.13: Implementation of a LinkedDeque class that inherits from the _DoublyLinkedBase class.
# first (real item just after header), last, 
# insert_first(self,e)(bu fonksiyon için _DoublyLinkedBase'deki insert between i kullan),
# insert_last(self,e),
# şu 2 fonksiyon için de _DoublyLinkedBase'den inherit edilen _delete_node metodunu kullan : 
# delete_first(self) silinen node'u döner, delete_last(self) silinen node'u döner
from _DoublyLinkedBase import _DoublyLinkedBase

class Empty(Exception):
    pass

class LinkedDeque(_DoublyLinkedBase): # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._trailer._prev._element

    def insert_first(self,e):
        self._insert_between(e,self._header,self._header._next)
    
    def insert_last(self,e):
        self._insert_between(e,self._trailer._prev,self._trailer)
    
    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._delete_node(self._trailer._prev)