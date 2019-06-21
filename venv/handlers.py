#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Vovien'

"""url handlers"""

from coroweb import get, post
import asyncio
from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }


@get('/api/comments')
def api_comments(*, page='1'):
    pass


@get('/blog/{id}')
def get_blog(id):
    pass
