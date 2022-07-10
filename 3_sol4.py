def coroutine():
    for i in range(1, 10):
        print("From generator {}".format((yield i)))
        print("i = ",i)

c = coroutine()
#c.send(None)
next(c)
print("after c.send(None)")
input()
c.send(987) # "From generator 987" yazar
input()
print(c.send(988)) # "From generator 987" ve "3" yazar
input()
try:
    while True:
        print("From user {}".format(c.send(1)))
        input()
except StopIteration: pass