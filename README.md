# try_pytest

pythonのTesting frameworkはいくつか在る。
openstackではunittestなのだが先輩からはpytestをススメられたのでそちらを少し試してみる。

[pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/latest/)

testコードやファイルの参照規則はこちら: https://docs.pytest.org/en/latest/goodpractices.html#test-discovery
参照規則++はこちら: https://docs.pytest.org/en/latest/example/pythoncollection.html

まあこっちは後で読めばいいか。

助かったやつ[pytest入門 - 闘うITエンジニアの覚え書き](https://www.magata.net/memo/index.php?pytest%C6%FE%CC%E7)


## pytest

```sh
$ ls -1
README.md
pytest.ini # conf
requirements.dev.txt
src
tests
virtualenv
```

- unitテストでは`src/tests`という構成になるのだとか。
    - >いくつかのパッケージの構成を見た限りでは、パッケージのディレクトリと同じ階層にテストディレクトリを作るのがセオリーらしい ( [Python 3 標準の unittest でテストを書く際のディレクトリ構成 - Qiita](https://qiita.com/hoto17296/items/fa0166728177e676cd36) )

- [pytest公式の考えはこれ](https://docs.pytest.org/en/latest/goodpractices.html). `src`と`test`で分けるタイプ。

```sh
setup.py
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py
```

[pytest-pythonpth](https://github.com/bigsassy/pytest-pythonpath)があるので、こいつを使うことにする。`pytest.ini`をすこしいじるだけで済む。

```sh
pip install pytest-pythonpath
```

## pytest-watch

```sh
pip install pytest-watchdog
ptw
```

べんり

## [pytest-aiohttp](https://aiohttp.readthedocs.io/en/stable/testing.html#pytest-example)

```sh
pip install pytest-aiohttp
```

おｋ，だいたいわかった。

## pydocってなに、どう書くの

```python
    def wrap_str(self, b):
        """
        ほげほげふがふが。コンストラクタで呼ばれる。

        Parameters
        ----------
        b : int
            bなんすよ…。aじゃないんすよ

        Returns
        -------
        str_b : str
            str(b)と同じ
        """

        return str(b)
```

### pydocの出力どうやんの

とりあえず下記でできるようだけれど、俺にはまだ早い感じがするので飛ばす。

```sh
pip install Sphinx
mkdir docs
cd docs
sphinx-quickstart #すげーだるい
sphinx-build -b html . build
cd ..
sphinx-apidoc -F -o docs/ src/
```
