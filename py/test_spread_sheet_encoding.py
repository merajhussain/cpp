from spread_sheet_encoding import spread_sheet_encoding


def test_spread_sheet_encoding1():
    assert 1==spread_sheet_encoding("A")

def test_spread_sheet_encoding2():
    assert 27==spread_sheet_encoding("AA")

def test_spread_sheet_encoding3():
    assert 55==spread_sheet_encoding("BC")

def test_spread_sheet_encoding4():
    assert 702==spread_sheet_encoding("ZZ")