# önce bir generator denemesi yapalım : 

def gentry(n):
    if n<0:
        yield 0
    yield n

print(next(gentry(-3)))
print(next(gentry(3)))
input()

# bir generator'ın son elemanını elde etme : 

def genx():
    for x in range(10):
        yield x

for last in genx():
    pass

print("Last element of genx is : ",last)
input()

def recursive_generator(lis):
    if lis:
        yield lis[0]
        yield from recursive_generator(lis[1:])

for k in recursive_generator([6,3,9,1]):
    print(k)

print("----------")
count = 0
while (count < 4):    
    count = count+1
    print(count)
    #break     # burada break olsaydı alttaki else çalışmazdı
else:
    print("No Break")

# Python 3.x program to check if an array consists
# of even number
def contains_even_number(l):
	for ele in l:
		if ele % 2 == 0:
			print ("list contains an even number")
			break

	# This else executes only if break is NEVER
	# reached and loop terminated after all iterations.
	else:	
		print ("list does not contain an even number")

# Driver code
print ("For List 1:")
contains_even_number([1, 9, 8])
print (" \nFor List 2:")
contains_even_number([1, 3, 5])
