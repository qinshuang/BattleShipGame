#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: models.py
@time: 2018/10/15
"""
from datetime import datetime
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_b = db.Column(db.Integer, nullable=False)
    user_w = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(80), default=1)
    user_active = db.Column(db.String(80), default='b')
    start_time = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __init__(self, user_b, user_w):
        self.user_b = user_b
        self.user_w = user_w

    def __repr__(self):
        return '<Match %r>' % self.id
