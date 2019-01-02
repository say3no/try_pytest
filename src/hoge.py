from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="hello world")


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
            bなんすよ…。aじゃないんすよ

        Returns
        -------
        str_b : str
            str(b)と同じ
        """

        return str(b)
