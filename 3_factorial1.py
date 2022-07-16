# faktöryel'i recursive hesaplayan bir fonks yaz

































def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)     

# faktöryel'i iterative hesaplayan bir fonksiyon yaz












def factorial2(n):
    sonuc=1
    for x in range(2,n+1):
        sonuc=sonuc*x
    return sonuc

print(factorial(4))
print(factorial2(4))