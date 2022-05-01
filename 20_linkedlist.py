# class LinkedList
# içinde __Node class var
# __init__ (x=LinkedList(y)), __getitem__(i) (a=x[i]), __setitem__(i,a) (x[i]=a), z=x.__add__(y) (z=x+y)
# x.append(a), x.insert(i,e) , x.__delitem__(i) (del x[i]) , x.__eq__(y) (x==y), x.__iter__() (for a in x:)
# x.__len__() (len(x)), x.__contains__(a) (a in x), ayrıca sort yazılabilir
# en başta bir dummy node kullan (değer içermeyecek)

class LinkedList:
    class __Node:     #
        __slots__ = '_value', '_next'
        def __init__(self, value):
            self._value = value
            self._next = None
            
    def __init__(self,contents=[]):
        self.first=self.__Node(None)  # dummy node, değer içermeyecek
        self.last=self.first
        self.size=0
        for e in contents:
            self.append(e)
    
    def __getitem__(self, index):
        if index>=0 and index<self.size:
            current=self.first._next
            for x in range(index):
                current=current._next
            return current._value
        else:
            raise IndexError("değeri istenen indeks geçersiz")
    
    def __setitem__(self,index, value):
        if index>=0 and index<self.size:
            current=self.first._next
            for x in range(index):
                current=current._next
            current._value = value
            return
        else:
            raise IndexError("değer atanmak istenen indeks geçersiz")
        
    def append(self,item):
        node=self.__Node(item)
        self.last._next=node
        self.last=node
        self.size += 1
    
    def insert(self,i,e):
        cursor = self.first._next
        for x in range(i-1):
            cursor=cursor._next
        a=cursor._next
        new=self.__Node(e)
        cursor._next=new
        new._next=a
        self.size+=1
        
#     def __add__(self,y):    # bu yazdığım self'e ekliyor y'yi, bu iyi olmadı
#                             # z=x+y olması için self+y şeklinde yeni bir linkedlist oluşturup onu dönmeli
#         y.first=y.first._next
#         self.last._next=y.first
#         self.last=y.last
#         self.size += y.size
#         return self
        
    def __add__(self,y):
        result=LinkedList()
        for i in self:
            result.append(i._value)
        for i in y:
            result.append(i._value)
        result.size=len(self)+len(y)
        return result
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        cursor=self.first._next
        while cursor!=None:
            yield cursor
            cursor=cursor._next
            
    def __delitem__(self,i):
        cursor=self.first
        for x in range(i):
            cursor=cursor._next
        tobedeleted=cursor._next
        cursor._next=cursor._next._next
        tobedeleted=None
        self.size-=1
        
    def __repr__(self):
        return ', '.join([str(x._value) for x in self])
        
    def __eq__(self,y):
        if len(self)!=len(y):
            return False
        cursor=y.first._next
        for i in self:
            if i._value != cursor._value:
                return False
            cursor = cursor._next
        return True
    
    def __contains__(self,e):
        for i in self:
            if i._value==e:
                return True
        return False

list1=LinkedList([1,2])
print(list1)
list1[1]=99
print(list1)
list1.append(3)
print(list1)
list2=LinkedList([4,5,6,7])
print(len(list1),len(list2))
list3=list1+list2  # list1 = list1 + list2 de çalışır
print(len(list3))
print(list3)
list3.insert(2,100)
print("before deletions :",list3,len(list3))
del list3[0]
del list3[4]
print("after deletions :", list3,len(list3))
if list3==list1:
    print(list1," ve ", list3, " aynı.")
else:
    print(list1," ve ", list3, " farklı.")
list1=LinkedList()
for i in list3:
    list1.append(i._value)
if list3==list1:
    print(list1," ve ", list3, " aynı.")
else:
    print(list1," ve ", list3, " farklı.")
if 99 in list1:
    print("list1'de 99 var.")
print("list1'de 2 var" if 2 in list1 else "list1'de 2 yok")