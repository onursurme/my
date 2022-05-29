# 1den 3e kadarki sayıların karelerini veren generator comprehension yazarak toplamını bul
# 1+4+9=14

print(sum(x*x for x in range(0,4)))

# aynı generator'a bir isim ver ve sonra toplamını bul

g1=(x*x for x in range(0,4))
print(sum(g1))

# 1den n'e kadarki (n dahil) tek sayıların karelerini veren bir list comprehension'ın toplamını dönen bir fonks yaz

def sumofodds(n):
    # return sum(x*x for x in range(1,n+1) if x%2==1) bu da olur alttaki de
    return sum([x*x for x in range(1,n+1) if x%2==1])

print(sumofodds(5))  #  1*1+3*3+5*5

# verilen bir iterable'ın (ör:range(1,5)) tersini dönderen bir fonks yaz (list comprehension kullansın)

def rev(data):
    return [data[len(data)-1-x] for x in range(0,len(data))]

data=[10,20,30,40]
print(rev(data))

# 0 1 1 2 3 5 8 .. şeklinde 100'den küçük fibonacci sayılarını veren bir generator yaz, ve generator'ı kullanarak ilk 10 sayıyı yazdır

def fib():
    f1,f2=0,1
    while f1<100:
        yield f1
        f1,f2=f2,f1+f2
        
f=fib()   # bu satırı yazmayıp 2 alta print(next(fibo())) yazarsak hep sıfır yazar çünkü fibo() hep baştan oluşur
for x in range(0,10):
    print(next(f))
    
# f'nin kalan değerlerini yazdıran bir for döngüsü yaz

for x in f:
    print(x)

# fib() generator'ü baştan başlatıp yazdıran bir for döngüsü yaz

for x in fib():
    print(x)

# sırayla 99,7 ve 1 sayılarını veren bir generator oluştur ve for döngüsü ile yazdır

def g2():
    yield 99
    yield 7
    yield 1
    
for x in g2():
    print(x)