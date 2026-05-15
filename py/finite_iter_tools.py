from itertools import *
import operator

print(list(accumulate(range(10))))

print (list(accumulate(range(1, 5), operator.mul)))


list1=[1,2,3]
list2=['a','b','c']
list3=['word1','word2','word3']

chained_list = chain(list1,list2,list3)

print(list(chained_list))




letters = ['a','b','c']
bools = [True, False, True]
compressed_list = compress(letters, bools)
print(list(compressed_list))



print (list(dropwhile(lambda x: x<5, [1,4,6,4,1,7])))

print (list(filterfalse(lambda x: x<5, [1,4,6,4,1,7])))


students = [('Atheeb', 'Scientist'), ('Afeef', 'Doctor'),
            ('Rafeeq', 'Engineer/Scholar'), ('Fatima', 'IAS'),
            ('Faazil', 'IPS'), ('Mehtaaj', 'Pilot'),
            ('Arzaan','CA'),('Nusrat','Professor')]

sorted_students = sorted(students)

for key,group in groupby(sorted_students, lambda profession:profession[0]):
    for student,profession in group:
        print(student,' :',profession,end='\n')



print("#############isslice##############")
iter = islice('meraj', 5)
i =0
while i<5:
    print(next(iter))
    i+=1
print("###################")

for i in islice(count(),1,10):
    print(i)


print("====starmap=====")
for item in starmap(lambda a,b: a+b, [(1,2),(2,3),(3,4)]):
    print(item)

print("###takewhile#######")
print (list(takewhile(lambda x: x<5, [1,4,6,4,1])))

print("####zip_longest####")
for item in zip_longest('ABCDEF','XYZ',fillvalue='*'):
    print(item)

