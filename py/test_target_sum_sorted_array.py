from targetsum import targetsum

def test_sorted_array_target_sum1():
    assert True == targetsum([2,7,11,15], 9)

def test_sorted_array_target_sum2():
    assert True == targetsum([3,2,4], 6)

def test_sorted_array_target_sum3():
    assert True == targetsum([3,3], 6)

def test_sorted_array_target_sum4():
    assert True == targetsum([1,2,3,4,5], 5)

def test_sorted_array_target_sum5():
    assert True == targetsum([1,1,1,2,2], 3)

def test_sorted_array_target_sum6():
    assert True == targetsum([0,0], 0)

def test_sorted_array_target_sum7():
    assert True == targetsum([0,1,2,3], 3)

def test_sorted_array_target_sum8():
    assert True == targetsum([-1,-2,-3,-4,-5], -8)

def test_sorted_array_target_sum9():
    assert True == targetsum([-1,0,1,2,-1,-4], 0)

def test_sorted_array_target_sum10():
    assert False == targetsum([10,20,30], 100)

def test_sorted_array_target_sum11():
    assert False == targetsum([1], 2)

def test_sorted_array_target_sum12():
    assert False == targetsum([], 0)