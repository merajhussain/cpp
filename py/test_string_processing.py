from string_processing import *

def test_first_upper_case():
    sp = string_processing()
    assert 'P'==sp.find_first_uppercase_character("Programming")

def test_str_len():
    sp = string_processing()
    assert 11==sp.strlen("Programming")

def test_count_consonants():
    sp = string_processing()
    assert 8 == sp.count_consonants("Programming")

def test_recursive_multiply():
    sp = string_processing()
    assert 40== sp.recursive_multiply(8,5)
