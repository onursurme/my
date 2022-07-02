import copy

def puzzle_solver(U,L,C):
    return

# permutation(k,S,U): k altküme uzunluğu, S boş, recursive
# U permütasyonu hesaplanacak olan küme (universal evrensel küme) 
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

# İNTERNETTEN BULDUĞUM YÖNTEMLER 

# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)

# Function to print permutations of string
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

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n)

# This code is contributed by Bhavya Jain


def permute(s, answer):
    if (len(s) == 0):
        print(answer, end = "  ")
        return
      
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)
  
# Driver Code
answer = ""
  
s = input("Enter the string : ")
  
print("All possible strings are : ")
permute(s, answer)
  
# This code is contributed by Harshit Srivastava

# Python function to print permutations of a given list
def permutation(lst):
    
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i+1:]
        
        # Generating all permutations where m is first
        # element
        
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
for p in permutation(data):
    print (p)