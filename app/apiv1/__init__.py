#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: __init__.py.py
@time: 2018/10/15
"""

from flask import Blueprint
from flask_restful import Api
from app.base.errors import errors

apiv1 = Blueprint('apiv1', __name__)
api = Api(apiv1,errors=errors)
from . import views
