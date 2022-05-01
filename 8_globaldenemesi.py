def dene():
    global glb1
    print("in function : ",glb1) #yukarıdaki global glb1 satırı olmasa bu satırda local variable "glb1" referenced before assignment hatası verir
    glb1="no"  
    print("in function : ",glb1)
    
glb1="yes"
dene()
print("in main     : ",glb1)