# n. fibonacci sayısını iterative hesaplayan fonksiyon yaz

# ardışık 2 fibonacci sayısını list olarak tutan bir generator yaz

# n. fibonacci sayısını veren binary recursive (her seferinde kendini 2 kez çağıran) fonks yaz
# neden kötü olduğunu açıkla

# girdi : n
# çıktı : [n. fibonacci sayısı, n-1. fibonacci sayısı]
# recursive fibonacci fonks yaz. bad_fibo'dan neden daha iyi olduğunu açıkla




















def fib(n):
    f1,f2=0,1
    for x in range(0,n):
        f1,f2=f2,f1+f2
    return f1

for x in range(5):
    print(x,fib(x))
input()
    
# ardışık 2 fibonacci sayısını list olarak tutan bir generator yaz

def fib2():
    a=[0,1]
    while True:
        yield a
        a[0],a[1]=a[1],a[0]+a[1]  # veya a=[a[1],a[0]+a[1]]
 
f2=fib2()
for x in range(10):
    print(next(f2))
    
# n. fibonacci sayısını veren binary recursive (her seferinde kendini 2 kez çağıran) fonks yaz
# neden kötü olduğunu açıkla

def bad_fib(n):
    if n<2:
        return n
    return bad_fib(n-1)+bad_fib(n-2)    # kötü olmasının (inefficient) nedeni : her çağrı kendini 2 kez çağırıyor
                                  # çağrı sayısı her seferinde x2 olduğu için üssel artıyor

for x in range(10):
    print(bad_fib(x))
    
# girdi : n
# çıktı : [n. fibonacci sayısı, n-1. fibonacci sayısı]
# recursive fibonacci fonks yaz. bad_fibo'dan neden daha iyi olduğunu açıkla

def good_fib(n):
    if n<2:
        return [n,n-1]
    x=good_fib(n-1)     # bad_fib'den daha iyi çünkü her çağrıda 2 kez değil 1 kez çağırıyor kendini
    return [x[0]+x[1],x[0]]  # böylece n arttıkça çağrı sayısı üstel değil lineer artıyor

for x in range(10):
    print(good_fib(x))
    
