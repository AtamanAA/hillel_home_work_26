import re


def find_email(text):
    pattern = "\S+[@]{1}\S+[.]{1}\w+"
    emails = re.findall(pattern, text)
    return emails


def test_find_email_valid_one():
    test_text = "Hello ataman@gmail.com"
    expected = ["ataman@gmail.com"]
    actual = find_email(test_text)
    assert expected == actual


def test_find_email_valid_many():
    test_text = "Hello ataman@gmail.com, ivan@fedorovich.com and dog@ua.com"
    expected = ["ataman@gmail.com", "ivan@fedorovich.com", "dog@ua.com"]
    actual = find_email(test_text)
    assert expected == actual


def test_find_email_valid_two_invalid_one():
    test_text = "Hello ataman@gmail.com, ivan@fedorovich.com and dog @ua.com"
    expected = ["ataman@gmail.com", "ivan@fedorovich.com"]
    actual = find_email(test_text)
    assert expected == actual


def test_find_email_without_email():
    test_text = "Hello ataman, ivan and @ua.com"
    expected = []
    actual = find_email(test_text)
    assert expected == actual
