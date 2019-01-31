#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: __init__.py.py
@time: 2019/01/29
"""

from flask_restplus import Namespace


ns = Namespace("users", description="Users CURD api.")

from . import views


@ns.errorhandler(Exception)
def specific_namespace_error_handler(error):
    '''Namespace error handler'''
    return {'message': getattr(error, 'message', str(error))}, getattr(error, 'code', 500)