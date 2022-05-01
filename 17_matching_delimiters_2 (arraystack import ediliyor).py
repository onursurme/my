"""Basic example of an adapter class to provide a stack interface to Python's list."""

from array_stack import ArrayStack


class Empty(Exception):
    pass

#   S = ArrayStack()                 # contents: [ ]
#   S.push(5)                        # contents: [5]
#   S.push(3)                        # contents: [5, 3]
#   print(len(S))                    # contents: [5, 3];    outputs 2
#   print(S.pop())                   # contents: [5];       outputs 3
#   print(S.is_empty())              # contents: [5];       outputs False
#   print(S.pop())                   # contents: [ ];       outputs 5
#   print(S.is_empty())              # contents: [ ];       outputs True
#   S.push(7)                        # contents: [7]
#   S.push(9)                        # contents: [7, 9]
#   print(S.top())                   # contents: [7, 9];    outputs 9
#   S.push(4)                        # contents: [7, 9, 4]
#   print(len(S))                    # contents: [7, 9, 4]; outputs 3
#   print(S.pop())                   # contents: [7, 9];    outputs 4
#   S.push(6)                        # contents: [7, 9, 6]
#   S.push(8)                        # contents: [7, 9, 6, 8]
#   print(S.pop())                   # contents: [7, 9, 6]; outputs 8


# • Correct: ( )(( )){([( )])}
# • Correct: ((( )(( )){([( )])}))
# • Incorrect: )(( )){([( )])}
# • Incorrect: ({[ ])}
# • Incorrect: (

def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['  # opening delimiters
    righty = ')}]'  # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False  # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return S.is_empty()  # were all symbols matched?


if is_matched("( )(( )){([( )])}"):
    print("1st is OK")
if is_matched("((( )(( )){([( )])}))"):
    print("2nd is OK")
if is_matched(")(( )){([( )])}"):
    print("3rd is OK")
if is_matched("({[ ])}"):
    print("4th is OK")
if is_matched("("):
    print("5th is OK")
