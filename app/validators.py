#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: validators.py
@time: 2018/10/22
"""
from serializers import MatchSchema
from marshmallow import ValidationError, fields


class ValidatedMatchSchema(MatchSchema):
    user_b = fields.Number(required=True)
    user_w = fields.Number(required=True)
