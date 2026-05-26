print(any([0,0,1,1,]))
print(any([0,0,0,0]))

print(any(['','','']))
print(any(['non empty','']))

my_str='my_string'
for position,val in enumerate(my_str):
    print(position,val)

my_list_string=['s1','s2','s3']
print(list(enumerate(my_list_string)))

marks_data=[91,92,45,70,60,50,100,99,75,85]

def filter_fun(x):
    return  x<75

for marks in filter(filter_fun,marks_data):
    print("what are u going to do with the future of students who socred",marks)

def to_upper(x):
    return x.upper()

my_list = ['a', 'b', 'c', 'd', 'e']
for item in map(to_upper, my_list):
    print(item)

keys=[1,2,3,4,5]
values=['a','b','c','d','e']

print(list(zip(keys,values)))
print(dict(zip(keys,values)))

