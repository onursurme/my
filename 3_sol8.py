# bu recursive fonksiyonu stack kullanarak iterative yapalım : 

# def recret(n):
#     if n<2:
#         return 1
#     return n * recret(n-1)

# print("recursive return : ")
# for i in range(6):
#     print(f"factorial({i}) = {recret(i)}")

def iteretws(n): # iterative function with stack. sanırım çok saçma oldu, yeniden yapılmalı ??!!!????!!!!
    stack=[n]
    result = 1
    while len(stack)>0:
        cv = stack.pop() # Current Value
        if cv<2:
            stack=[]
        else:
            result = result * cv
            stack.append(n-1)
            n = n - 1
    return result

print("iterative return with stack : ")
for i in range(6):
    print(f"factorial({i}) = {iteretws(i)}")