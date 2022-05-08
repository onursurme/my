# bir positional list'i artan sıraya sokan insertion sort, sayfa 285
#
# We maintain a variable named marker that represents the rightmost position of
# the currently sorted portion of a list. During each pass, we consider the position just
# past the marker as the pivot and consider where the pivot’s element belongs relative
# to the sorted portion; we use another variable, named walk, to move leftward from
# the marker, as long as there remains a preceding element with value larger than the pivot’s.

def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreasing order."""