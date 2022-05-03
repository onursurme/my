# A PositionalList class based on a doubly linked list
# p.element( ): Return the element stored at position p.
# accessor methods:
# L.first( ): Return the position of the first element of L, or None if L is empty.
# L.last( ): Return the position of the last element of L, or None if L is empty.
# L.before(p): Return the position of L immediately before position p, or None if p is the first position.
# L.after(p): Return the position of L immediately after position p, or None if p is the last position.
# L.is_empty( ): Return True if list L does not contain any elements.
# len(L): Return the number of elements in the list.
# iter(L): Return a forward iterator for the elements of the list. See Section # 1.8 for discussion of iterators in Python.
# (iter için first, element, after metodlarını kullan)
# update methods:
# L.add_first(e): Insert a new element e at the front of L, returning the position of the new element.
# L.add_last(e): Insert a new element e at the back of L, returning the position of the new element.
# L.add_before(p, e): Insert a new element e just before position p in L, returning the position of the new element.
# L.add_after(p, e): Insert a new element e just after position p in L, returning the position of the new element.
# L.replace(p, e): Replace the element at position p with element e, returning the element formerly at position p.
# L.delete(p): Remove and return the element at position p in L, invalidating the position.

from _DoublyLinkedBase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # -------------------------- nested Position class --------------------------
    class Position:
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            # burayı anlamadım
            return type(self) is type(other) and other._node is self._node

        def __ne__(self, other):
            # self!=other olmaz mı, neden is kullanmadık?
            return not (self == other)

        def __repr__(self):
            return str("Position info :", self._container+" "+self._node._element)

    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(self.Position):
            raise TypeError("not a position")
        if not (self == p._container):
            raise ValueError("p doesn't belong to this container")
        if p._node._next is None:  # if p._node._next == None: ile aynı mı
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):  # first, element, after metodlarını kullan
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = cursor.after()

        # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        return self._make_position(super()._insert_between(e, predecessor, successor))

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):  # insert between'i kullan
        node=self._validate(p)
        return self._insert_between(e,node._prev,node)

    def add_after(self, p, e):
        node=self._validate(p)
        return self._insert_between(e,node,node._next)

    def delete(self, p):
        node=self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p."""
        node=self._validate(p)
        old=node._element
        node._element=e
        return old


L = PositionalList()
print(L.add_last(8))      # p
print(L)  # 8p
print(L.first())          # p
print(L)  # 8p
print(L.add_after(p, 5))   # q
print(L)  # 8p, 5q
print(L.before(q))        # p
print(L)  # 8p, 5q
print(L.add_before(q, 3))  # r
print(L)  # 8p, 3r, 5q
print(r.element())        # 3
print(L)  # 8p, 3r, 5q
print(L.after(p))         # r
print(L)  # 8p, 3r, 5q
print(L.before(p))        # None
print(L)  # 8p, 3r, 5q
print(L.add_first(9))     # s
print(L)  # 9s, 8p, 3r, 5q
print(L.delete(L.last()))  # 5
print(L)  # 9s, 8p, 3r
print(L.replace(p, 7))     # 8
print(L)  # 9s, 7p, 3r

# eg:
# Operation          Return Value L
# L.add_last(8)      p            8p
# L.first()          p            8p
# L.add_after(p,5)   q            8p, 5q
# L.before(q)        p            8p, 5q
# L.add_before(q,3)  r            8p, 3r, 5q
# r.element()        3            8p, 3r, 5q
# L.after(p)         r            8p, 3r, 5q
# L.before(p)        None         8p, 3r, 5q
# L.add_first(9)     s            9s, 8p, 3r, 5q
# L.delete(L.last()) 5            9s, 8p, 3r
# L.replace(p,7)     8            9s, 7p, 3r
