# vim: set fileencoding=utf-8 :
from src.hoge import Hoge


def test_constractor():
    a = 1
    b = 2
    hoge = Hoge(a, b)
    assert hoge.a == 1
    assert hoge.b == 2
