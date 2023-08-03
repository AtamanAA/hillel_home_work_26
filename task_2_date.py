import re


def validate_date(date):
    #  Validate date format MM/DD/YYYY
    pattern = "^(0?[1-9]|1[0-2])/(0?[1-9]|[1-2]{1}[0-9]{1}|3[0-1]{1})/[0-9]{4}$"
    date = re.search(pattern, date)
    return bool(date)


def test_validate_date_valid_1():
    test_date = "10/29/1990"
    expected = True
    actual = validate_date(test_date)
    assert expected == actual


def test_validate_date_valid_2():
    test_date = "01/01/2025"
    expected = True
    actual = validate_date(test_date)
    assert expected == actual


def test_validate_date_invalid_month():
    test_date = "20/01/2000"
    expected = False
    actual = validate_date(test_date)
    assert expected == actual


def test_validate_date_invalid_day():
    test_date = "02/39/2000"
    expected = False
    actual = validate_date(test_date)
    assert expected == actual


def test_validate_date_invalid_year():
    test_date = "02/19/200"
    expected = False
    actual = validate_date(test_date)
    assert expected == actual


def test_validate_invalid_date_type():
    test_date = "twenty january 2020"
    expected = False
    actual = validate_date(test_date)
    assert expected == actual


def test_validate_zero_number():
    test_date = "00/00/0000"
    expected = False
    actual = validate_date(test_date)
    assert expected == actual
