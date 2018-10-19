#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: serializers.py
@time: 2018/10/18
"""

from flask_marshmallow import Schema
from app.models import User


class UserSchema(Schema):
    class Meta:
        model = User
        fields = ('username', 'email')

