# vim: set fileencoding=utf-8 :
from src.hoge import Hoge

# @pytest.fixture(scope='session', autouse=True)
# def session_fixture():
#    print("テスト全体の前処理")
#    yield
#    print("テスト全体の後処理")


def test_constractor():
    a, b = (1, 2)
    h = Hoge(a, b)
    assert h.a == a
    assert h.b == str(b)
