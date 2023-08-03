import re


def validate_phone(number):
    pattern = "^[+]?([0-9]+ *-* *){2}[(]?([0-9]+ *-* *){3}[)]?([0-9]+ *-* *){7}$"
    phone = re.search(pattern, number)
    return bool(phone)


def test_valid_phone_valid_1():
    test_phone = "+380955518311"
    expected = True
    actual = validate_phone(test_phone)
    assert expected == actual


def test_valid_phone_valid_2():
    test_phone = "+3 8095 55 183 11"
    expected = True
    actual = validate_phone(test_phone)
    assert expected == actual


def test_valid_phone_valid_3():
    test_phone = "+3-8095-55-183-11"
    expected = True
    actual = validate_phone(test_phone)
    assert expected == actual


def test_valid_phone_valid_4():
    test_phone = "+3 - 8095 - 55-183-11"
    expected = True
    actual = validate_phone(test_phone)
    assert expected == actual


def test_valid_phone_valid_5():
    test_phone = "+38(095)5518311"
    expected = True
    actual = validate_phone(test_phone)
    assert expected == actual


def test_valid_phone_invalid():
    test_phone = "+38(095)551831"
    expected = False
    actual = validate_phone(test_phone)
    assert expected == actual
