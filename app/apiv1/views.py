#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2018/10/15
"""

from flask import request
from . import api
from app import db
from flask_restful import Resource, reqparse

from marshmallow import ValidationError
from app.models import User, Match
from app.serializers import UserSchema, MatchSchema
from app.validators import ValidatedMatchSchema
from app.handles.mixins import BaseMixin
import json

parser = reqparse.RequestParser()
parser.add_argument('pk', type=int, help='PK cannot be converted')


class UserView(Resource):
    def get(self, user_id):
        user = db.session.query(User).all()
        us = UserSchema().dump(user, many=True)
        return us

    def put(self, user_id):
        return {}


class MatchView(Resource):
    def get(self):
        match_id = parser.parse_args().get('pk', None)
        match = BaseMixin().get_obj_by_id(Match, match_id)
        return MatchSchema().dump(match)

    def post(self):
        result = ValidatedMatchSchema().loads(request.data)
        if result.errors:
            return result.errors
        match = Match(user_b=result.data.get('user_b'), user_w=result.data.get('user_w'))
        BaseMixin().create(match)
        return MatchSchema().dump(match)


api.add_resource(UserView, '/user/<int:user_id>')
api.add_resource(MatchView, '/match/detail/')
