from itertools import *


for item in count(start=0,step=2):

    if item > 100:
        break
    print(item)



it = repeat(10,3)
for i in range (0,3):
    print(next(it))


count=0
for item in cycle('AB'):
    if count == 6:
        break
    print(item)
    count+=1






