# Code Fragment 7.13: Implementation of a LinkedDeque class that inherits from the _DoublyLinkedBase class.
# first (real item just after header), last, insert_first(self,e), insert_last(self,e),
# delete_first(self) silinen node'u döner, delete_last(self) silinen node'u döner

class LinkedDeque(_DoublyLinkedBase): # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""
    