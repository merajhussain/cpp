import time

from func_tools import *

def test_lru_cache():
    s1   = time.perf_counter()
    fibval1= fib_no_cahce(35)
    e1= time.perf_counter()
    elapsed1 = e1 - s1
    s2= time.perf_counter()
    fibval2 = fib_lru_cache(35)
    e2 = time.perf_counter()
    elapsed2 = e2 - s2
    assert elapsed1 > elapsed2 and fibval1 == fibval2