from string_permutation import is_string_permutation


def test_string_permutaion1():
    assert True == is_string_permutation("listen","silent")

def test_string_permutaion2():
    assert False == is_string_permutation("abc","ab")

def test_string_permutaion3():
    assert False == is_string_permutation("abc","abd")

def test_string_permutaion4():
    assert False == is_string_permutation("aabb","abbb")

def test_string_permutaion5():
    assert True == is_string_permutation("Dormitory","Dirty room")