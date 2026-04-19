from functools import lru_cache,partial

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