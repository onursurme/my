# U isimli bir listin k uzunluktaki permütasyonlarını
# yield eden, return eden, yazdıran
# recursive ve iterative
# 6 çeşit fonksiyon yaz
# combinatiom da yaz

# permutation(k,S,U): k altküme uzunluğu, S boş, recursive
# U permütasyonu hesaplanacak olan küme (universal, evrensel küme) 
# S boş (ipucu: en sonunda yine boş oluyor)
# fonksiyon permütasyonları return etmiyor, S'e koyuyor
# permütasyonlar fonk içinde print ediliyor






















def permutation2(k,S,U):   # bunu sonraki tekrarda kendim yazdım
    if k==0:
        print(S)
    for i in U:
        S.append(i)
        permutation2(k-1,S,[x for x in U if x not in S])
        S.remove(i)

permutation2(4,[],[1,2,3,4])
input()


def permutation(k,S,U):
    if k==1:
        print(S+U)
        return
    for x in range(len(U)):
        a=U[x]
        S.append(a)
        U.remove(a)
        permutation(k-1,S,U)
        S.remove(a)
        U.insert(x,a)
        
data=[1,2,3,4]
permutation(4,[],data)