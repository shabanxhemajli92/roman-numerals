from roman import roman_to_numeral
def test_roman():
    assert roman_to_numeral('XXI') == 21
    assert roman_to_numeral('I') == 1
    assert roman_to_numeral('IV') == 4
    assert roman_to_numeral('MMVII') == 2007
    assert roman_to_numeral('MDCLXV') == 1665
