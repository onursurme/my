# stack yaz (class ArrayStack:   _data adında bir list kullansın arka planda)
# init,len, is_empty, top(boşsa hata versin), pop(boşsa hata versin), 
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
#
#  bu stack yapısını kullanarak şu fonksiyonu yaz :
#  def is_matched(expr): """Return True if all delimiters are properly match; False otherwise."""
# • Correct: ( )(( )){([( )])}
# • Correct: ((( )(( )){([( )])}))
# • Incorrect: )(( )){([( )])}
# • Incorrect: ({[ ])}
# • Incorrect: (
# hatalar için şu Empty class'ı kullan : 
class Empty(Exception):
    pass

# test kodları : 
# if is_matched("( )(( )){([( )])}"):
#     print("1st is OK")
# if is_matched("((( )(( )){([( )])}))"):
#     print("2nd is OK")
# if is_matched(")(( )){([( )])}"):
#     print("3rd is OK")
# if is_matched("({[ ])}"):
#     print("4th is OK")
# if is_matched("("):
#     print("5th is OK")

# S = ArrayStack()  Empty exception'ı denemek için yazdım
# S.pop()
class ArrayStack:
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty("stack boş ki") 
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty("stack boş ki")
        return self._data.pop()
    
def is_matched(expr):
    stack=ArrayStack()
    opening=['(','{','[']
    closing=[')','}',']']
    for x in expr:
        if x in opening:
            stack.push(x)
        elif x in closing:
            # buraya if stack boşsa koymak lazım, çünkü expr kapama ile başlıyorsa alttaki stack.top() hata veriyor
            if stack.top()==opening[closing.index(x)]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    return False
    
    
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