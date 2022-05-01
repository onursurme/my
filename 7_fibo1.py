# n. fibonacci sayısını iterative hesaplayan fonksiyon yaz






























def fibo1(n):   # iterative (yani not recursive)
    if n<2:
        return n
    a1,a2=0,1
    for x in range(0,n-1):
        a1,a2=a2,a1+a2
    return a2

# şu da olur :
def fib(n):
    f1,f2=0,1
    for x in range(0,n):
        f1,f2=f2,f1+f2
    return f1

print(fibo1(4))
print(fib(4))
# ardışık 2 fibonacci sayısını list olarak tutan bir generator yaz


























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




















def good_fibo(n):  # kitapta 1 yerine 2 değer dönen recursive bir Fibonacci fonksiyonu verilmiş
                   # bad_fibo her seferinde 2 recursive call yaptığı için nonefficient.
                   # burada ise tek çağrı hedeflenmiş
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





def fibo4(n):   # n 0 veya 1 değeriyle başlayıp giderek artan sırada çağrılırsa hiç miss alınmıyor
                # ama bunu yapmadan direk fibo4(10) gibi bir çağrı yapılırsa miss'ler yaşanıyor
                # recursive (fibo3'ten daha efficient). burada amacım daha önce hesaplanan değerlerin yeniden hesaplanmamasını
                # sadece "daha önce hesaplanmamış olan" değerlerin  hesaplanmasını sağlamak
                # bu yaklaşımın neresi zayıf/geliştirilebilir : baştan 100 uzunlukta array açıldı, fazla gelirse, yetmezse?
    global last # bunu yazmazsak aşağıda last'ı kullanmak istediğimizde last'ı bu fonksiyona ait lokal bir değişken zanneder ve
                # değer atamadan kullanıyorsun diye hata verir
    if last>=n:
        print("hit : ", n)
        return fibo4data[n]
    if last<n-2:
        print("miss :", n-2," last=",last)
        fibo4data[n-2]=fibo4(n-2)
        last=n-2   # daha küçük bir terim hesaplanmadan daha büyük terim hesaplanamaz
                   # yani n-2'yi hesaplıyorsak o ana kadar hesapladğımız en büyük terim n-2. terim demektir

    if last<n-1:
        print("miss :",n-1," last=",last)
        fibo4data[n-1]=fibo4(n-1)
        last=n-1
    fibo4data[n]=fibo4data[n-2]+fibo4data[n-1]
    last=n
    print(n,"=",n-2,"(hit) +",n-1," (hit)  last=",last)
    return fibo4data[n]


fibo4data=[0]*100
fibo4data[0]=0
fibo4data[1]=1
last=1
print("sonuç = ",fibo4(13))
print("sonuç = ",fibo4(16))
print("sonuç = ",fibo4(8))

print(fibo4data)
print("----------------------------")
for x in range(10):
    print(x," : ",fibo4(x))
print("last",last)
print(fibo4data[:last+1])

# for x in range(0,10):
#     print(x+1," : ",fibo4(x))
# print(fibo4data)
    
# f2=fibo2()
# for x in range(0,10):
#     print(x+1," : ",next(f2))