# pow1(x,n)  x'in n. kuvvetini döner. recursive


























def pow1(x,n):        # benim yazdığım recursive. kitap diyor ki bundan çok daha hızlı bir yolu var. pow2 de bunu araştırdım
    if n==0:          # if n==1:  return x   de olur
        return 1
    return x*pow1(x,n-1)

# pow1'in daha hızlı çalışanı yazılabilir. pow2(x,n)
# alttaki çözümün daha iyisi olabilir
# her pozitif tamsayı 2'nin farklı pozitif tamsayı kuvvetlerinin toplamı olarak yazılabilir
# hangi kuvvetlerin toplamı olduğunu bulmanın en kolay yolu sayıyı binary'ye çevirmektir
# bir integer'ı binary'ye çevirip basamakları bir list yapmanın hızlı ve kolay bir yolu : [int(x) for x in bin(8)[2:]]









def pow2(x,n):       # kitap der ki pow1'dekinden çok daha hızlı bir yolu var, pow2'de bunu araştırdım
                     # galiba yolu şu : örneğin x^2 yi bulduğunda bunu kendisiyle çarpıp x^4ü elde etmek vs vs
                     # böylece n yerine logn olur
                     # evet, şimdi kitaptakine baktım, doğru düşünmüşüm
                     # benim sona eklediğim pow2(x,n-n//2-n//2) kitaptakinden farklı olmuş, orada n odd mu even mı ona bakmışlar
    if n==0:
        return 1
    if n==1:
        return x
    return pow2(x,n//2)*pow2(x,n//2)*pow2(x,n-n//2-n//2) #burası şöyle olabilir if x even return pow2*pow2 else return pow2*pow2*x

def pow2cached(x,n):  # functools cache lru kullanılabilirdi
    cache=dict()
    cache[0]=1
    cache[1]=x
    cache[2]=x*x
    if n<3:
        return cache[n]
    k,r=2,cache[2]
    while k<n:
        for key in sorted(cache, reverse=True):
            value=cache[key]
            #print(key,value,k,r)
            #input()
            if k*key<=n:
                print(n,k,key,cache)
                input()
                k=k+key
                r=r*value
                cache[k*key]=r
                #print("new",key,value,k,r)
                break
    #print(cache)
    return r

from functools import lru_cache

@lru_cache()
def pow2lru(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    return pow2lru(x,n//2)*pow2lru(x,n//2)*pow2lru(x,n-n//2-n//2) #burası şöyle olabilir if x even return pow2*pow2 else return pow2*pow2*x


# pow3(x,n) iterative


























def pow3(x,n):     # benim yazdığım iterative
    result=1
    for y in range(n):
        result*=x
    return result

print(pow1(2,5))
print(pow2(3,4))
print(pow3(2,5))