#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: __init__.py.py
@time: 2019/01/30
"""
from flask import Blueprint
from flask_restplus import Api

errors_blueprint = Blueprint("errors", __name__)
api = Api(errors_blueprint, version="1.0", title="ErrorsAPI", description="The Errors Api", doc='/doc/')

