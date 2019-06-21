#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    for i in range(10):
        u = User(name='Test_%s' % i, email='test%s@example.com' % i, password='1234567890', image='about:blank')
        await u.save()


# 要运行协程，需要使用事件循环
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    print('Test finished.')
    loop.run_forever()
