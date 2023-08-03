import re


def find_sentences(text):
    pattern = "\S[^!?.]+[.?!]+"
    sentences = re.findall(pattern, text)
    return sentences


def test_find_sentences_valid_one():
    test_text = (
        "The sun was setting behind the mountains, casting a warm glow over the valley."
    )
    expected = [
        "The sun was setting behind the mountains, casting a warm glow over the valley."
    ]
    actual = find_sentences(test_text)
    assert expected == actual


def test_find_sentences_valid_five():
    test_text = (
        "The sun was setting behind the mountains, casting a warm glow over the valley... "
        "Birds were chirping merrily, bidding farewell to the day... "
        "A gentle breeze rustled the leaves on the trees, creating a soothing melody? "
        "In the distance, a river meandered gracefully through the landscape, colors of the sky! "
        "As darkness descended, the stars began to twinkle, painting the night with their celestial brilliance."
    )
    expected = [
        "The sun was setting behind the mountains, casting a warm glow over the valley...",
        "Birds were chirping merrily, bidding farewell to the day...",
        "A gentle breeze rustled the leaves on the trees, creating a soothing melody?",
        "In the distance, a river meandered gracefully through the landscape, colors of the sky!",
        "As darkness descended, the stars began to twinkle, painting the night with their celestial brilliance.",
    ]
    actual = find_sentences(test_text)
    assert expected == actual


def test_find_sentences_invalid():
    test_text = "..."
    expected = []
    actual = find_sentences(test_text)
    assert expected == actual


def test_find_sentences_empty():
    test_text = ""
    expected = []
    actual = find_sentences(test_text)
    assert expected == actual
