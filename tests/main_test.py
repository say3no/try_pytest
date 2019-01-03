import pytest
from aiohttp import web
from src.main import routes as routing


# async def previous(request):
#    if request.method == 'POST':
#        request.app['value'] = (await request.post())['value']
#        return web.Response(body=b'thanks for the data')
#    return web.Response(
#        body='value: {}'.format(request.app['value']).encode('utf-8'))


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    app.add_routes(routing)
    return loop.run_until_complete(aiohttp_client(app))


async def test_hello(cli):
    resp = await cli.get('/')
    assert resp.status == 200
    assert await resp.text() == 'hello world'

    # async def test_set_value(cli):
    #    resp = await cli.post('/', data={'value': 'foo'})
    #    assert resp.status == 200
    #    assert await resp.text() == 'thanks for the data'
    #    assert cli.server.app['value'] == 'foo'
    #
    #
    # async def test_get_value(cli):
    #    cli.server.app['value'] = 'bar'
    #    resp = await cli.get('/')
    #    assert resp.status == 200
    #    assert await resp.text() == 'value: bar'
    #
