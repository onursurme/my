# 1den n'e kadarki tek sayıların karelerini veren bir list comprehension'ın toplamını dönen bir fonks yaz 





























def f1(n):
    return sum([k*k for k in range(1,n) if k%2==1])
    
print(f1(4))
input()

for x in range(8,-10,-2):
    pass
#    print(x)    8 6 4....-6 -8 yazar
    
for x in [2**k for k in range(0,9)]:
    pass
#    print(x)   1 2 4 .... 128 256 yazar

# verilen bir iterable'ın (ör:range(1,5)) tersini dönderen bir fonks yaz (list comprehension kullansın)














def inverser(a):
    b=[a[len(a)-1-x] for x in range(0,len(a))]
    return b

a=range(1,5)
for y in inverser(a):
    print(y)

# 0 1 1 2 3 5 8 .. şeklinde ilk 100 fibonacci sayısını veren bir generator yaz, ve generator'ı kullanarak ilk 10 sayıyı yazdır











def fib():
    q1=0
    q2=1
    #q1,q2=0,1
    while q1<100:
        yield q1
        q1,q2=q2,q1+q2
        
f=fib()
for x in range(0,10):
    print(next(f))

# f'nin kalan değerlerini yazdıran bir for döngüsü yaz













for x in afi:   # bu şekilde afinin kalanını verir
    print(x)
    
# fib() generator'ü baştan başlatıp yazdıran bir for döngüsü yaz











for x in fib():   # bu şekilde fib baştan başlar
    print(x)

print("-------------------------------")

# sırayla 99,7 ve 1 sayılarını veren bir generator oluştur ve for döngüsü ile yazdır








def gen_deneme():
    yield 99
    yield 7
    yield 1
    
for x in gen_deneme():
    print(x)
    