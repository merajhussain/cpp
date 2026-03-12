from functools import reduce

#lambdas
square = lambda x: x*x
print(square(5))

add = lambda a, b: a + b
print(add(2,3))

#map
nums = [1,2,3,4]
result = list(map(lambda x: x*x, nums))

print(result)

print([x*x for x in nums])


#filter
nums = [1,2,3,4,5,6]

evens = list(filter(lambda x: x%2==0, nums))

print(evens)

print([x for x in nums if x%2==0])



#reduce
nums = [1,2,3,4]
result = reduce(lambda x,y: x+y, nums)
print(result)