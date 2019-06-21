#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging;

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Asesome<h1>', content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", '/', index)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    await site.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
