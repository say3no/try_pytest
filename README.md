# try_pytest

pythonのTesting frameworkはいくつか在る。
openstackではunittestなのだが先輩からはpytestをススメられたのでそちらを少し試してみる。

[pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/latest/)

testコードやファイルの参照規則はこちら: https://docs.pytest.org/en/latest/goodpractices.html#test-discovery
参照規則++はこちら: https://docs.pytest.org/en/latest/example/pythoncollection.html

まあこっちは後で読めばいいか。

## pydocってなに、どう書くの

```python
    def wrap_str(self, b):
        """
        ほげほげふがふが。コンストラクタで呼ばれる。

        Parameters
        ----------
        b : int
            bなんすよ…。

        Returns
        -------
        str_b : str
            str(b)と同じ
        """

        return str(b)
```

## pydocの出力どうやんの

```sh
pip install Sphinx
sphinx-quickstart #すげーだるい
```


## pytestのconfigってどうなってるの

## task-runnerみたいなやつとかどうなってるの