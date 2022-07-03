# faktöryel'i recursive  hesaplayan 3 fonksiyon yaz
#     1'den başlayarak sayıların faktöryellerini yield eden,
#     verilen bir n sayısının faktöryelini return eden
#     verilen bir n sayısının faktöryelini print eden
# bu fonksiyonları stack kullanarak iterative hale getir
# stack kullanmadan iterative versiyonlarını da yaz
# bu fonksiyonları kıyasla

# recursive yield
# recursive return
# recursive print
# iterative yield with stack
# iterative return with stack
# iterative print with stack
# iterative yield without stack
# iterative return without stack
# iterative print without stack

def recyield():
    sonuc = 1
    x = 0
    while True:
        yield sonuc
        x = x + 1
        sonuc = sonuc * x

rc=recyield()
print("recursive yield : ")
for i in range(10):
    print(f"factorial({i}) = {next(rc)}")

input()

def recret(n):
    if n<2:
        return 1
    return n * recret(n-1)

print("recursive return : ")
for i in range(10):
    print(f"factorial({i}) = {recret(i)}")

input()

def recprnt_old(n,f):
    if n<2:
        if n==f:
            print(f"factorial({n}) = 1")
            return
        else:
            return 1
    if n==f:
        print(f"factorial({n}) = {n * recprnt(n-1,f)}")
    else:
        return n*recprnt(n-1,f)

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
for i in range(10):
    recprnt(i)

input()




















def faktoryel(n):
    if n==1:
        return 1
    return n*faktoryel(n-1)

for x in range(1,7):
    print(faktoryel(x))
    
# faktöryel'i iterative hesaplayan bir fonksiyon yaz

def faktoryel2(n):
    sonuc = 1
    for x in range(1,n+1):
        sonuc = sonuc * x
    return sonuc

for x in range(1,7):
    print(faktoryel2(x))