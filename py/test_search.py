
from array_search import *
import time



def test_linear_search1():
    arr = [1,3,5,7,9,11]
    index = linear_search(arr,15)
    expected = -1
    assert index == expected


def test_linear_search2():
    arr = [1,3,5,7,9,11]
    index = linear_search(arr,5)
    expected = 2
    assert index == expected

def test_binary_search1():
    arr = [1,3,5,7,9,11]
    index = binary_search(arr,15)
    expected = -1
    assert index == expected


def test_binary_search2():
    arr = [1,3,5,7,9,11]
    index = binary_search(arr,5)
    expected = 2
    assert index == expected

def test_performace():
    arr = [x for x in range(100000000)]
    s1 = time.perf_counter()
    i1=linear_search(arr, 100000000)

    e1 = time.perf_counter()
    elapsed1 = e1 - s1
    print()
    print("Linear search elapsed time:",format(elapsed1, '.15f'))
    s2 = time.perf_counter()
    i2=binary_search(arr, 100000000)
    e2 = time.perf_counter()
    elapsed2 = e2 - s2
    print("Binary search elapsed:",format(elapsed2, '.15f'))
    assert elapsed1 > elapsed2 and i1==i2

def test_fixed_point1():
    arr = [-10, -5, 0, 3, 7]
    assert 3 == fixed_number(arr)

def test_fixed_point2():
    arr = [0, 2, 5, 8, 17]
    assert 0 == fixed_number(arr)

def test_fixed_point3():
    arr = [-10, -5, 3, 4, 7, 9]
    assert None == fixed_number(arr)

def test_biotonic_peak1():
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    assert 5 == biotonic_peak(arr)

def test_biotonic_peak2():
    arr = [1, 6, 5, 4, 3, 2, 1]
    assert 6 == biotonic_peak(arr)

def test_biotonic_peak3():
    arr = [5, 4, 3, 2, 1]
    assert 5 == biotonic_peak(arr)

def test_biotonic_peak4():
    arr = [1,2,3,4,5]
    assert None == biotonic_peak(arr)

def test_integer_square_root():
    assert 17 == integer_sqrt(300)

def test_integer_square_root_2():
    assert 3 == integer_sqrt(12)

def test_closest_number1():
    assert 9 == closest_number([2, 5, 9, 12], 8)

def test_closest_number2():
    assert 5 == closest_number([1, 3, 5, 7], 5)

def test_closest_number3():
    assert 10 == closest_number([10, 20, 30], 5)

def test_closest_number4():
    assert 30 == closest_number([10, 20, 30], 40)

def test_closest_number5():
    assert 6 == closest_number([6, 8], 7)  # tie → smaller

def test_closest_number6():
    assert 4 == closest_number([2, 4, 4, 4, 6, 8], 5)

def test_closest_number7():
    assert 7 == closest_number([7, 7, 7, 7], 10)

def test_closest_number8():
    assert -5 == closest_number([-10, -5, -2, 0, 3], -4)

def test_closest_number9():
    assert 100 == closest_number([100], 50)