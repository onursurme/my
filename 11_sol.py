# pow1(x,n)  x'in n. kuvvetini döner. recursive

def pow1(x,n):
    if n==1:
        return x
    return x*pow1(x,n-1)    

print(pow1(2,3))

# pow1'in daha hızlı çalışanı yazılabilir. pow2(x,n)
# pow1'in daha hızlı çalışanı yazılabilir. pow2(x,n)
# 11_power1.py'de yaptığım çözümün daha iyisi olabilir diye düşünüyorum
# her pozitif tamsayı 2'nin farklı pozitif tamsayı kuvvetlerinin toplamı olarak yazılabilir
# hangi kuvvetlerin toplamı olduğunu bulmanın en kolay yolu sayıyı binary'ye çevirmektir
# bir integer'ı binary'ye çevirip basamakları bir list yapmanın hızlı ve kolay bir yolu : [int(x) for x in bin(8)[2:]]

def pow2(x,n):
    pass
    

# pow3(x,n) iterative

def pow3(x,n):
    result=1
    for i in range(n):
        result = result * x
    return result

print(pow3(2,3))