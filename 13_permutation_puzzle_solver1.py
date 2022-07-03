import copy
from itertools import product

# U isimli bir listin k uzunluktaki permütasyonlarını
# yield eden, return eden, yazdıran
# recursive ve iterative
# 6 çeşit fonksiyon yaz
# combination için de aynı fonksiyonları yaz

# permutation(k,S,U): k altküme uzunluğu, S boş bir list, recursive
# U permütasyonu hesaplanacak olan list (universal, evrensel küme) 
# S boş gidiyor, boş dönüyor
# fonksiyon permütasyonları return etmiyor, S'e koyuyor
# permütasyonlar fonk içinde print ediliyor























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
        
# permutation(k,S,U): k altküme uzunluğu, S boş bir list, recursive
# U permütasyonu hesaplanacak olan set (universal, evrensel küme) 
# fonksiyon permütasyonları return etmiyor, S'e koyuyor
# permütasyonlar fonk içinde print ediliyor

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
permutation(k,S,U)
input()
print("permutation 2 :")
permutation2(k,S,U)
input()
print("S after permutation and permutation2 : ",S)
input()
print("permutation 3 :")
permutation3(k,S,{1,2,3})
input()

# DİĞER YÖNTEMLER 

# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)

# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print (toString(a))
    else:
        for i in range(l,r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

string = "ABC"
n = len(string)
a = list(string)
print("permute :")
permute(a, 0, n)
print()
input()

def permute2(s, answer):
    if (len(s) == 0):
        print(answer, end = "  ")
        return
      
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute2(rest, answer + ch)
  
answer = ""
s = "ABC"
print("permute2 :")
permute2(s, answer)
input()
print()
  
def permutation4(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = [] # empty list that will store current permutation

    for i in range(len(lst)):
        m = lst[i]
        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i+1:]
        # Generating all permutations where m is first element
        for p in permutation4(remLst):
            l.append([m] + p)
    return l

data = list('123')
print("permutation4 : ")
for p in permutation4(data):
    print (p)

input()

# başka bir tane
def permutation5(lis):
    if len(lis) == 1:
        return [lis]
    output = []
    *front, last = lis
    for perm in permutation5(front):
        for i in range(len(perm) + 1):
            new = perm[:i] + [last] + perm[i:]
            output.append(new)
    return sorted(output)

print("permutation5 : ")
print(permutation5([1,2,3]))
input()

def permute3(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute3(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute3(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

print("permute3 : ")
for p in permute3([1, 2, 3]):
    print(p)

input()

# permute array
#     if array is of size 2
#        return first and second element as new array
#        return second and first element as new array
#     else
#         for each element in array
#             new subarray = array with excluded element
#             return element + permute subarray


def permute4(u):   # böyle yield ile çalışıyor ama print eden veya return eden versiyonlarını yazamadım (permute5 ve 6, aşağıda)
    if len(u)==0:
        yield []
    for i in u:
        for j in permute4([x for x in u if x != i]):
            yield [i]+j

print("permute4 : ")
p4=permute4(['x','y','z'])
for i in p4:
    print(i)

input()

def permute5(u,ln):  # iyi değil, flat yapmaya, uzunluk kontrolüne gerek olmamalı, geliştirilmeli
    if len(u)==1:
        return u
    result=[]
    for i in u:
        for j in permute5([x for x in u if x != i],ln):
            result.append([i]+[j])
    flatr=[]   # buradan sonrası hile gibi, yukarısı düzelirse buraya gerek kalmaz, liste içindeki listeleri yok ettim
    for i in result:
        i=[x for xs in i for x in xs]
        flatr.append(i)
        if len(i)==ln:
            print(i)
    return flatr

print("permute5 : ")
permute5(['x','y','z'],3)
input()

def permute6(u):   # iyi değil, flat yapmaya gerek kalmamalı, geliştirilmeli
    if len(u)==1:
        #print("len=1",u)
        return u
    result=[]
    for i in u:
        r=permute6([x for x in u if x != i])
        for j in range(len(r)):
            #print("result before appending :",result)
            result.append([i]+[r[j]])  # burada extend denedim, 2 değer arasına , ve + denedim
            #print("result appended :",result)
    #print("returning result :",result)
    flatr=[]   # buradan sonrası hile gibi, yukarısı düzelirse buraya gerek kalmaz, liste içindeki listeleri yok ettim
    for i in result:
        i=[x for xs in i for x in xs]
        flatr.append(i)
    return flatr

p6=permute6(['x','y','z'])
print("permute6 : ")
print(p6)
input()

# ITERATIVE (recursive her fonksiyon stack kullanarak iterative yapılabilir)
def perms(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

print("perms : ")
print(perms("abc"))
input()

def permutations6(head, tail=''):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            permutations6(head[:i] + head[i+1:], tail + head[i])

print("permutations6 : ")
permutations6("onr")
input()

def permutations7(elements):
    if len(elements) <= 1:
        yield elements
        return
    for perm in permutations7(elements[1:]):
        for i in range(len(elements)):
            # nb elements[0:1] works in both string and list contexts
            yield perm[:i] + elements[0:1] + perm[i:]

print("permutations7 : ")
print(list(permutations7("ONR")))
input()
        
def permutations8(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):  # itertools'un product fonksiyonu kullanılıyor
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

print("permutations8 : ")
print(list(permutations8("ONR")))
input()

def perm9(a, k=0):
   if k == len(a):
      print(a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm9(a, k+1)
         a[k], a[i] = a[i], a[k]

print("perm9 : ")
perm9([1,2,3])