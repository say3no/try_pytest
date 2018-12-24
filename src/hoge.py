class Hoge:
    """ A simple example class """

    def __init__(self, a, b):
        self.a = a
        self.b = self.wrap_str(b)

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
