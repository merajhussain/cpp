from functools import lru_cache,partial,singledispatch

@lru_cache(maxsize=100)
def fib_lru_cache(n):
    if n < 2:
        return n
    return fib_lru_cache(n-1) + fib_lru_cache(n-2)

print(fib_lru_cache(35))  # Fast because of caching

def fib_no_cahce(n):
    if n < 2:
        return n
    return fib_no_cahce(n-1) + fib_no_cahce(n-2)

print(fib_no_cahce(35))


def add(a,b):
    return a+b

def mul(a,b):
    return a*b

addp=partial(add,2,3)
mulp=partial(mul,3,4)

print(addp())
print(mulp())


@singledispatch
def show_obj(obj):
    print("default version of",obj)

@show_obj.register
def _(obj:int):
    print("Int version of ",obj)

@show_obj.register(str)
def _(obj):
    print("str version of ",obj)

show_obj(1)
show_obj(2.0)
show_obj("hi")
