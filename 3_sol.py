# faktöryel'i recursive  hesaplayan fonksiyon türleri
#     0'den başlayarak sayıların faktöryellerini yield eden,
#     verilen bir n sayısının faktöryelini return eden
#     verilen bir n sayısının faktöryelini print eden
# bu fonksiyonları stack kullanarak iterative hale getir
# stack kullanmadan iterative versiyonlarını da yaz
# bu fonksiyonları kıyasla

# kendimce 7 çeşit fonskiyon belirledim : 
# 1- recursive yield (sürekli sıradakini üreten ve verilen bir n sayısının faktöryelini üreten diye 2 çeşit olabilir)
# 2- recursive return
# 3- recursive print
# 4- iterative yield without stack (sürekli sıradakini üreten ve verilen bir n sayısının faktöryelini üreten diye 2 çeşit olabilir)
# 5- iterative return/print without stack
# 6- iterative yield with stack (recursive'in stack kullanılarak iterative'e dönüştürülmüş hali) (sürekli sıradakini üreten ve verilen bir n sayısının faktöryelini üreten diye 2 çeşit olabilir)
# 7- iterative return/print with stack (recursive'in stack kullanılarak iterative'e dönüştürülmüş hali)
# 4 ile 6, 5 ile 7 farklılar mı bilmiyorum, deneyip görelim : 

def recyield2(n=0,f=0): # 0'dan başlayarak sıradaki sayının faktöryelini dönen recursive generator 
    while True:
        if n<2:
            yield 1
            if f==1:
                return
        else:
            for prev in recyield2(n-1,1):
                pass
            yield prev * n
            if f==1:
                return
        n = n + 1

print("recursive yield 2 (continuous) : ")
ry2=recyield2()
for i in range(6):
    print(f"factorial({i}) = {next(ry2)}")

input()

def recyield(n): # belirli bir n sayısının faktöryelini dönen recursive generator 
    if n<2:
        yield 1
        return
    for prev in recyield(n-1):
        pass
    yield prev * n
    
print("recursive yield (belli bir n) : ")
for i in range(6):
    print(f"recursive yield ({i}) : {next(recyield(i))}")

input()

def recret(n):
    if n<2:
        return 1
    return n * recret(n-1)

print("recursive return : ")
for i in range(6):
    print(f"factorial({i}) = {recret(i)}")

input()

def recprnt(n,f=0): # fonksiyon ilk çağrıldığında f=0 , recursive çağrılarda ise f=1 oluyor
    if n<2:
        if f==0:
            print(f"factorial({n}) = 1")
            return
        else:
            return 1
    if f==0:
        print(f"factorial({n}) = {n * recprnt(n-1,1)}")
    else:
        return n * recprnt(n-1,f)

print("recursive print() : ")
for i in range(6):
    recprnt(i)

input()

# iter yield without stack
# iter return/print without stack

def iteryield():   # sürekli sıradakini veren
    sonuc = 1
    x = 0          # iterreturn'deki for yerine burada x=0 while ve x=x+1 satırları var
    while True:
        yield sonuc
        x = x + 1
        sonuc = sonuc * x

print("iterative yield without stack : ")
iy=iteryield()
for i in range(6):
    print(f"factorial({i}) = {next(iy)}")

input()

def iteryield2(n):   # n sayısının faktöryelini veren
    sonuc = 1
    for x in range(1,n+1):
        sonuc = sonuc * x
    yield sonuc
    return

print("iterative yield without stack 2 : ")
for i in range(6):
    print(f"iterative yield ({i}) : {next(iteryield2(i))}")

input()

def iterreturn(n):
    sonuc = 1
    for x in range(1,n+1):
        sonuc = sonuc * x
    return sonuc    # stack'siz iterprint'in tek farkı bu satırda return etmeyip print etmesi

print("iterative return without stack : ")
for x in range(6):
    print(iterreturn(x))

input()

# iter yield with stack
# iter return with stack
