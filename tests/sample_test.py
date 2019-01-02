# vim: set fileencoding=utf-8:


def main():
    func(3)


def func(x):
    for ele in range(19):
        print(ele)

    return x + 1


"""
ビルトインの機能である assert を使ったテスト
"""


def test_answer():
    assert func(4) == 5


if __name__ == "__main__":
    main()
