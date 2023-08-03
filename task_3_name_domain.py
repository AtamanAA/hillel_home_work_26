import re


def get_name_domain(email):
    pattern = "^(\w+)@(\w+[.]\w+)$"
    match_phrase = re.match(pattern, email)
    try:
        name, domain = match_phrase.groups()
        return {"name": name, "domain": domain}
    except AttributeError:
        return {"Error": "Invalid email"}


def test_get_name_domain_valid():
    test_date = "ataman@gmail.com"
    expected = {"name": "ataman", "domain": "gmail.com"}
    actual = get_name_domain(test_date)
    assert expected == actual


def test_get_name_domain_invalid_email():
    test_date = "test ataman@gmail.com"
    expected = {"Error": "Invalid email"}
    actual = get_name_domain(test_date)
    assert expected == actual


def test_get_name_domain_invalid_email_name():
    test_date = "gmail.com"
    expected = {"Error": "Invalid email"}
    actual = get_name_domain(test_date)
    assert expected == actual


def test_get_name_domain_invalid_domain():
    test_date = "test ataman@gmailcom"
    expected = {"Error": "Invalid email"}
    actual = get_name_domain(test_date)
    assert expected == actual
