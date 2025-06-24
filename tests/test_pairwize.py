import pytest
from allpairspy import AllPairs

parametrs = [
    ['Windows', 'MacOs', "Linux"],
    ['Chrome', 'FF', "Yandex"],
    ['EN', 'RU', "KO", "IN"]
]



@pytest.mark.parametrize(["os", "browser", "lang"], [values for values in AllPairs(parametrs)])
def test_allpairspy(os, browser, lang):
    print(os, browser, lang)

