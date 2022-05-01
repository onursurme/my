# A PositionalList class based on a doubly linked list
# p.element( ): Return the element stored at position p.
# In the context of the positional list ADT, positions serve as parameters to some
# methods and as return values from other methods. In describing the behaviors of a
# positional list, we being by presenting the accessor methods supported by a list L:
# L.first( ): Return the position of the first element of L, or None if L is empty.
# L.last( ): Return the position of the last element of L, or None if L is empty.
# L.before(p): Return the position of L immediately before position p, or None
# if p is the first position.
# L.after(p): Return the position of L immediately after position p, or None if
# p is the last position.
# L.is empty( ): Return True if list L does not contain any elements.
# len(L): Return the number of elements in the list.
# iter(L): Return a forward iterator for the elements of the list. See Section
# 1.8 for discussion of iterators in Python.
# The positional list ADT also includes the following update methods:
# L.add first(e): Insert a new element e at the front of L, returning the position
# of the new element.
# L.add last(e): Insert a new element e at the back of L, returning the position
# of the new element.
# L.add before(p, e): Insert a new element e just before position p in L, returning
# the position of the new element.
# L.add after(p, e): Insert a new element e just after position p in L, returning
# the position of the new element.
# L.replace(p, e): Replace the element at position p with element e, returning
# the element formerly at position p.
# L.delete(p): Remove and return the element at position p in L, invalidating
# the position.
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

class PositionalList( DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #-------------------------- nested Position class --------------------------
    class Position:
        def init (self, container, node):
        """Constructor should not be invoked by user."""
            self. container = container
            self. node = node
        
        def element(self):
            
        def __eq__(self, other):
            
        def __ne__(self, other):
            
    def _validate(self,p):
        """Return position s node, or raise appropriate error if invalid."""
        
    def make position(self, node):
    """Return Position instance for given node (or None if sentinel)."""
    
    def first(self):
        
    def last(self):
        
    def before(self,p):
        
    def after(self,p):
    
    def __iter__(self):
        
    # override inherited version to return Position, rather than Node
    def insert between(self, e, predecessor, successor):
        
    def add_first(self, e):
    """Insert element e at the front of the list and return new Position"""
    
    def add_last(self, e):
        
    def add_before(self, p, e):
        
    def add_after(self, p, e):
        
    def delete(self,p):
    
    def replace(self,p,e):
    """Replace the element at Position p with e.
       Return the element formerly at Position p."""
    