# bu recursive fonksiyonu stack kullanarak iterative yapalım : 

# def recret(n):
#     if n<2:
#         return 1
#     return n * recret(n-1)

# print("recursive return : ")
# for i in range(6):
#     print(f"factorial({i}) = {recret(i)}")

def iteretws(n): # iterative with stack
    STACK = []
    STACK.insert(0, ['CALL',{'n':n}])
    RESULT = None
    while STACK:
        #print("STACK=",STACK)
        #print("RESULT=",RESULT)
        action,data = STACK.pop(0)
        #print("action=",action,"data=",data)
        if action == 'CALL':
            n = data['n']
            if n==1:
                RESULT=1
            else:
                STACK.insert(0,['RESUME',{'n':n}])
                STACK.insert(0,['CALL',{'n':n-1}])
        else:
            RESULT = RESULT * data['n']
    return RESULT

print("iterative return with stack : ")
print(f"factorial(3) = {iteretws(3)}")

def fibonacci(n):
    STACK = []
    CACHE = {0: 0, 1: 1}

    STACK.insert(0,['CALL',{'n':n}])
    RESULT = 0

    while STACK:
        action, data = STACK.pop(0)
        if action == 'CALL':
            n = data['n']
            if n in CACHE:
                RESULT += CACHE[n]
            else:
                STACK.insert(0,['RESUME',{'n':n}])
                STACK.insert(0,['CALL',{'n':n-2}])
                STACK.insert(0,['CALL',{'n':n-1}])
        elif action == 'RESUME':
            n = data['n']
            CACHE[n] = RESULT
    return RESULT

print([fibonacci(n) for n in range(15)])