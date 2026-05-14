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