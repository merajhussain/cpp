from is_palindrom_permutaion import is_palindrome_permutation

def test_palindrome_permutaion1():
    assert True == is_palindrome_permutation("aabb")

def test_palindrome_permutaion2():
    assert True == is_palindrome_permutation("aabbc")

def test_palindrome_permutaion3():
    assert False == is_palindrome_permutation("aabbcd")

def test_palindrome_permutaion4():
    assert True == is_palindrome_permutation("Tact Coa")

def test_palindrome_permutaion5():
    assert True == is_palindrome_permutation("")
