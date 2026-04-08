from is_anagram import is_anagram


def test_is_anagram1():
    assert True == is_anagram("conversation","voices rant on")

def test_is_anagram2():
    assert True == is_anagram("A gentleman","Elegant man")

def test_is_anagram3():
    assert False == is_anagram("abc","bc")
