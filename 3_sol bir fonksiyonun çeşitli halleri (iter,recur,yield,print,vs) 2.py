def recyield3(n=0,f=0): # 0'dan başlayarak sıradaki sayının faktöryelini print eden recursive generator 
    while True:
        if n<2:
            if f==1:
                yield 1
                return # recursive bir çağrıyla gelindiyse o generator'ı sonlandır
            else:
                print("1")
                yield 1
        else:
            for prev in recyield3(n-1,1): # n-1'in faktöryelini hesaplayan generator'ün son değeri prev oluyor
                pass
            if f==1:
                yield prev * n
                return
            else:
                print(prev*n)
                yield prev*n
        n = n + 1

print("recursive yield 3 (continuous) : ")
ry3=recyield3()
for i in range(6):
    next(ry3)

input()

# iter print without stack cont

def iterprintcontwithoutstack(): 
    sonuc = 1
    x = 0 
    while True:
        print(f"factorial({x}) = {sonuc}")
        yield
        x = x + 1
        sonuc = sonuc * x

print("iterative print without stack (continuous) : ")
iy=iterprintcontwithoutstack()
for i in range(6):
    next(iy)

input()

def iteryieldprint(n):   # iterative yield without stack, n sayısının faktöryelini veren
    sonuc = 1
    for x in range(1,n+1):
        sonuc = sonuc * x
    print(sonuc)
    yield sonuc
    return

print("iterative yield without stack 2 (belli bir n) : ")
iyp=iteryieldprint()
for i in range(6):
    next(iyp)