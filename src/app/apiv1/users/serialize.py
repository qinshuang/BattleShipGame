#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: serialize.py
@time: 2019/01/02
"""
# from flask_marshmallow import Schema
# from marshmallow import fields
from flask_restplus import fields
from app.apiv1.users import ns

role_schema = ns.model('RoleModel', {
    'id': fields.String(required=True, readonly=True, description="unique id"),
    'name': fields.String(description='The name', required=True),
})

user_schema = ns.model('UserModel', {
    'id': fields.String(required=True, readonly=True, description="unique id"),
    'email': fields.String(description="unique id"),
    'username': fields.String(description="unique id"),
    'active': fields.String(description="unique id"),
    'first_name': fields.String(description="unique id"),
    'last_name': fields.String(description="unique id"),
    'roles': fields.List(fields.Nested(role_schema, many=True))

})
