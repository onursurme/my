import copy

def puzzle_solver(U,L,C):
    return

# permutation(k,S,U): k altküme uzunluğu, S boş, U universal yani evrensel küme, recursive
# S boş gidiyor, boş dönüyor
# fonksiyon permütasyonları return etmiyor, S'e koyuyor, fonk içinde S print ediliyor














def permutation(k,S,U):   # benim yazdığım. kitaptaki ile farkı?
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


def permutation2(k,S,U):  # kitaptaki. s176 pseudocode verilmiş ve U bir set, ben burada list yaptım
    U2=copy.copy(U)       # kitaptakinde bu satır yoktu, çalışmayınca ben ekledim (?)
    for x in U2:
        S.append(x)
        #print("S : ",S)
        U.remove(x)
        #print("U : ",U)
        if k==1:
            print("result :",S) # bir puzzle çözüyorsak burada print yerine sonucu deneyebiliriz
        else:
            permutation2(k-1,S,U)
        S.remove(x)
        U.append(x)   # set olsaydı U.add() olacaktı
        
def permutation3(k,S,U):  # kitaptaki. bu kez U'yu set yaptım kitaptaki gibi.
    U2=copy.copy(U)       # kitaptakinde bu satır yoktu, çalışmayınca ben ekledim (?)
                          # set olunca sadece son satırda U.append(x) yerine U.add(x) geliyor
    for x in U2:
        S.append(x)
        #print("S : ",S)
        U.remove(x)
        #print("U : ",U)
        if k==1:
            print("result :",S) # bir puzzle çözüyorsak burada print yerine sonucu deneyebiliriz
        else:
            permutation3(k-1,S,U)
        S.remove(x)
        U.add(x)   # set olsaydı U.add() olacaktı

k=3
S=[]
U=[1,2,3]
permutation2(k,S,U)
print(S)
permutation3(k,S,{1,2,3})
# U2=copy.copy(U)
# for x in U2:
#     S.append(x)
#     print("S : ",S)
#     U.remove(x)
#     print("U : ",U)
    
U={ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
L={'b','o','y','g','i','r','l','a','d','c','t','p','n'}
C1="pot+pan=bib"
C2="dog+cat=pig"
C3="boy+girl=baby"
C=[C1,C2,C3]