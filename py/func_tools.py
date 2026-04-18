from functools import lru_cache

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