import copy

# permutation(k,S,U): k altküme uzunluğu, S boş, recursive
# U permütasyonu hesaplanacak olan küme (universal, evrensel küme) 
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
permutation2(k,S,U)
input()
print(S)
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
permute(a, 0, n)
print()


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
s = input("Enter the string : ")
print("All possible strings are : ")
permute2(s, answer)
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
for p in permutation4(data):
    print (p)

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

print(permutation5([1,2,3]))
