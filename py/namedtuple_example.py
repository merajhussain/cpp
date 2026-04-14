from collections import namedtuple

Book = namedtuple('Book', ('name', 'Author', 'pages'))
b1 = Book("Quran","Allah",1000)
print(b1)

House = namedtuple('House', ('area', 'type','floor','model'))
h1 = House(900,'individual',1,'3-BHK')
print(h1)

Car = namedtuple('Car', ('name', 'model', 'year'))
c1 = Car('Mercedes', model='g wagon', year=1999)
print(c1)

Phone = namedtuple('Phone', ('name', 'model', 'os','price'))
p1 =  Phone("Apple","17 pro max","ios",150000)
p2 =  Phone("Google","Pixel 9","Android",80000)
print(p1)
print(p2)


