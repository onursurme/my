# n. fibonacci sayısını iterative hesaplayan fonksiyon yaz






























def fibo1(n):   # iterative (yani not recursive)
    if n<2:
        return n
    a1,a2=0,1
    for x in range(n-1): # range(0,n-1) ile range(n-1) aynı
        a1,a2=a2,a1+a2
    return a2

# şu da olur :
def fib(n):
    f1,f2=0,1
    for x in range(n):
        f1,f2=f2,f1+f2
    return f1

print(fibo1(4))
print(fib(4))
# ardışık 2 fibonacci sayısını list olarak tutan ve her çağrıldığında sıradaki fibonacci sayısını veren bir generator yaz


























def fibo2():    # generator
    a=[0,1]
    while True:
        yield a[0]
        a=[a[1],a[0]+a[1]]

# n. fibonacci sayısını veren binary recursive (her seferinde kendini 2 kez çağıran) fonks yaz
# neden kötü olduğunu açıkla






















def bad_fibo(n):   # çok kötü çünkü n 1 arttığında çağrılan fonksiyon sayısı 2 katına çıkıyor
    if n<2:
        return n
    return bad_fibo(n-1) + bad_fibo(n-2)

# girdi : n
# çıktı : [n. fibonacci sayısı, n-1. fibonacci sayısı]
# recursive fibonacci fonks yaz. bad_fibo'dan neden daha iyi olduğunu açıkla




















def good_fibo(n):  # bad_fibo her seferinde 2 recursive call yaptığı için nonefficient.
                   # burada ise tek çağrı yapıldığı için daha efficient
    if n<2:
        return [n,0]
    s=good_fibo(n-1)
    return [s[0]+s[1],s[0]]

for x in range(10):
    twofibos=good_fibo(x)
    print("good_fibo :",twofibos[0],' , ',twofibos[1]) # x. fibo sayısı good_fibo(x)[0]
input()

# bu soruyu ben düşündüm : 
# o ana kadar hesapladığı fibonacci sayılarını fibo4data[] listesinde biriktiren
# o ana kadar hesapladığı en büyük fibonacci sayısının sıra numarasını global olan ve last isimli bir değişkende tutan
# şu şekilde kullanılan :
# fibo4data=[0]*100
# fibo4data[0]=0
# fibo4data[1]=1
# last=1
# print("sonuç = ",fibo4(13))
# zaten daha önce hesapladığı bir değeri boşuna tekrar hesaplamayıp fibo4data'dan dönderen
# recursive fibonacci fonksiyonunu yaz
# girdi : n   çıktı : n. fibonacci sayısı




lasty=1

def fibo4(n):   # n 0 veya 1 değeriyle başlayıp giderek artan sırada çağrılırsa hiç miss alınmıyor
                # ama bunu yapmadan direk fibo4(10) gibi bir çağrı yapılırsa miss'ler yaşanıyor
                # recursive (fibo3'ten daha efficient). burada amacım daha önce hesaplanan değerlerin yeniden hesaplanmamasını
                # sadece "daha önce hesaplanmamış olan" değerlerin  hesaplanmasını sağlamak
                # bu yaklaşımın neresi zayıf/geliştirilebilir : baştan 100 uzunlukta array açıldı, fazla gelirse, yetmezse?
    global lasty # bunu yazmazsak aşağıda last'ı kullanmak istediğimizde last'ı bu fonksiyona ait lokal bir değişken zanneder ve
                # değer atamadan kullanıyorsun diye hata verir
                # bknz globaldegisken_python.py isimli programım
    if lasty>=n:
        print("hit : ", n)
        return fibo4data[n]
    if lasty<n-2:
        print("miss :", n-2," last=",lasty)
        fibo4data[n-2]=fibo4(n-2)
        lasty=n-2   # daha küçük bir terim hesaplanmadan daha büyük terim hesaplanamaz
                   # yani n-2'yi hesaplıyorsak o ana kadar hesapladğımız en büyük terim n-2. terim demektir

    if lasty<n-1:
        print("miss :",n-1," last=",lasty)
        fibo4data[n-1]=fibo4(n-1)
        lasty=n-1
    fibo4data[n]=fibo4data[n-2]+fibo4data[n-1]
    lasty=n
    print(n,"=",n-2,"(hit) +",n-1," (hit)  last=",lasty)
    return fibo4data[n]


fibo4data=[0]*100
fibo4data[0]=0
fibo4data[1]=1
print("sonuç = ",fibo4(13))
print("sonuç = ",fibo4(16))
print("sonuç = ",fibo4(8))

print(fibo4data)
print("----------------------------")
for x in range(10):
    print(x," : ",fibo4(x))
print("last",lasty)
print(fibo4data[:lasty+1])

# for x in range(0,10):
#     print(x+1," : ",fibo4(x))
# print(fibo4data)
    
# f2=fibo2()
# for x in range(0,10):
#     print(x+1," : ",next(f2))

# bu yaptığım memoization'ın Python'ın bir özelliğini kullanarak yapılması : 

from functools import lru_cache

@lru_cache()
def fibonacci(n):
    print('Enter', n)
    if n==0:
        x = 0
    elif n==1:
        x = 1
    else:
        x = fibonacci(n-1) + fibonacci(n-2)
    print('Exit', n)
    return x

print(fibonacci(4))

# diğer bir memoization (benim fibo4 ün daha basit hali)

cache = dict()

def fibonacci2(n):
    if n in cache:
        return cache[n]
    if n==0:
        x = 0
    elif n==1:
        x = 1
    else:
        x = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = x
        return x

print(fibonacci2(4))