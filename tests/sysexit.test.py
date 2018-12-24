# vim: set fileencoding=utf-8 :
from src.hoge import Hoge


def test_constructor():
    a = Hoge("a", 222)
    print(a.a)
    print(a.b)
