# disjoint ve disjoint2 isimli fonksiyonların big-Oh 'larını bul
# bu fonksiyonlar A kesişim B kesişim C boş kümeyse True dönüyorlar
# cevap en alttaa, zaten program çalıştırılınca da sonuç ortaya çıkıyor (?)

def disjoint(A,B,C):
    count=0
    for a in A:
        for b in B:
            for c in C:
                count+=1
                print(count)
                if a==c:
                    return False
    return True

def disjoint2(A,B,C):
    count=0
    for a in A:
        for b in B:
            if a==b:   # bu satır n^2 kez çalışır, en fazla n kez a==b olup aşağı ilerle
                for c in C:
                    count+=1  # bu satır ve altındaki 2 satır en fazla n^2 kez çalışır
                    print(count)
                    if a==c:
                        return False
    return True

# A B ve C 'yi worst-case olacağını düşündüğüm şekilde belirledim : 
A=[1,2,3,4,5]
B=[1,2,3,4,5]
C=[6,7,8,9,10]

print(disjoint(A,B,C))
input()
print(disjoint2(A,B,C))

# cevap: disjoint O(n^3) , disjoint2 ise O(n^2)
# açıklaması : disjoint2'de a==b en fazla n kez sağlanır, altındaki C döngüsü de en fazla n kez çalışır, n^2 yapar.