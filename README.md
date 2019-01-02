# try_pytest

pythonのTesting frameworkはいくつか在る。
openstackではunittestなのだが先輩からはpytestをススメられたのでそちらを少し試してみる。

[pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/latest/)

testコードやファイルの参照規則はこちら: https://docs.pytest.org/en/latest/goodpractices.html#test-discovery
参照規則++はこちら: https://docs.pytest.org/en/latest/example/pythoncollection.html

まあこっちは後で読めばいいか。

## pytest

```sh
$ ls -1
README.md
requirements.txt
src
tests
virtualenv
```

こういう構成にして、`tests`をウオッチしてタスクランナーを走らせたい。

## pytest-watch

```sh
pip install pytest-watchdog

```

## pytest-aiohttp

```sh
pip install pytest-aiohttp
```

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
