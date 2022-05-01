# faktöryel'i recursive hesaplayan bir fonks yaz

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