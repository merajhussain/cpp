from itertools import *
import operator

print(list(accumulate(range(10))))

print (list(accumulate(range(1, 5), operator.mul)))


list1=[1,2,3]
list2=['a','b','c']
list3=['word1','word2','word3']

chained_list = chain(list1,list2,list3)

print(list(chained_list))
