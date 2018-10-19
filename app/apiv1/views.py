#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2018/10/15
"""

from . import api
from app import db
from flask_restful import Resource

from app.models import User
from app.serializers import UserSchema


class UserView(Resource):
    def get(self, user_id):
        user = db.session.query(User).all()
        us = UserSchema().dump(user, many=True)
        return us

    def put(self, user_id):
        return {}


api.add_resource(UserView, '/user/<int:user_id>')
