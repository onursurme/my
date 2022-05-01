import sys

# bir sistemde iç içe kaç recursive çağrı yapılabileceğinin sınırını test eden bir program yaz
# global bir count=0 değişkeni olsun
# her recursive çağrıda count 1 artsın ve ekrana yazılsın


















# ... to combat against infinite recursions, the designers of
# Python made an intentional decision to limit the overall number of function activations
# that can be simultaneously active. The precise value of this limit depends
# upon the Python distribution, but a typical default value is 1000. If this limit is
# reached, the Python interpreter raises a RuntimeError with a message, maximum
# recursion depth exceeded.

def a():
    global count
    count+=1
    print(count)
    if count>900:
        return
    a()
    
old=sys.getrecursionlimit()
print("old recursion limit is : ",old)
input()
count=0
a()
count=0
sys.setrecursionlimit(100) # programın çalışması bitince yine default value olan 1000 geçerli oluyor
a()
