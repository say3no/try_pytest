# vim: set fileencoding=utf-8 :
import pytest
from src.hoge import Hoge

# @pytest.fixture(scope='session', autouse=True)
# def session_fixture():
#    print("テスト全体の前処理")
#    yield
#    print("テスト全体の後処理")


def test_constractor():
    a, b = (1, 2)
    reg = Hoge(a, b)
    assert hasattr(reg, 'a')
    assert hasattr(reg, 'b')
    assert reg.a == a
    assert reg.b == str(b)
    assert str(b) in reg.b

    # errorはこんなかんじ
    with pytest.raises(TypeError) as e:
        irr = Hoge()


# pytest.raises(SomeError)のかわりに、
# こういったデコレータでも異常系のテストを書ける。便利
@pytest.mark.xfail(raises=TypeError)
def test_pytest_error():
    irr = Hoge()
