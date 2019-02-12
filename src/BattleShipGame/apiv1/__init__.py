#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: __init__.py.py
@time: 2019/01/29
"""

from flask import Blueprint
from flask_restplus import Api
from .users import ns as user_api

apiv1_blueprint = Blueprint("apiv1", __name__)
apiv1 = Api(apiv1_blueprint, version="1.0", title="OpenApi", description="The Open Api Service", doc='/doc/')

apiv1.add_namespace(user_api)

