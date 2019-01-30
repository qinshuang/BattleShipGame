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