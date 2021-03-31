from aiohttp import web
import asyncio
import aiohttp
import json

# web.Response(text=resp['value'])
url1 = {'url': 'https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random',
        'headers': {'accept': "application/json",
                    'x-rapidapi-key': "2c2801d0aemsh468c72e7ac284a8p1c5336jsnc10155942577",
                    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"},
        'params': None}

# web.Response(text=str(resp['data']))
url2 = {'url': 'https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total',
        'headers': {'x-rapidapi-key': "2c2801d0aemsh468c72e7ac284a8p1c5336jsnc10155942577",
                    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"},
        'params': {"country": "Ukraine"}}

# web.Response(text=str(resp[0]['text']))
url3 = {'url': 'https://brianiswu-cat-facts-v1.p.rapidapi.com/facts',
        'headers': {'x-rapidapi-key': "2c2801d0aemsh468c72e7ac284a8p1c5336jsnc10155942577",
                    'x-rapidapi-host': "brianiswu-cat-facts-v1.p.rapidapi.com"},
        'params': None}

list_url = [url1, url2, url3]
routes = web.RouteTableDef()


async def get(site, headers, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(site, headers=headers, params=params) as response:
            print("Status:", response.status)
            html = await response.text()
            return html


async def response():
    text = []
    for url in list_url:
        response_json = await get(url['url'], headers=url['headers'], params=url['params'])
        resp = json.loads(response_json)
        if url == url1:
            text.append(resp['value'])
        elif url == url2:
            text.append(str(resp['data']))
        elif url == url3:
            text.append(str(resp[0]['text']))
    return text


@routes.get('/collect_info')
async def info(request):
    result = await response()
    return web.Response(text='\n\n'.join(result))

app = web.Application()
app.add_routes(routes)
web.run_app(app, host='localhost')
