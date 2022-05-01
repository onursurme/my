# permutation(k,S,U): k altküme uzunluğu, S boş, U universal yani evrensel küme, recursive
# S boş gidiyor, boş dönüyor
# fonksiyon permütasyonları return etmiyor, S'e koyuyor, fonk içinde S print ediliyor

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