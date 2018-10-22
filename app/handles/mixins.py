#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: mixins.py
@time: 2018/10/19
"""

# todo: init map and ships
# todo: ship dispose to map
# todo: save map
# todo: start game
# todo: click map and check
# todo: show ship
from app import db


class BaseMixin(object):

    def create(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get_obj_by_id(self, T, id):
        return db.session.query(T).filter(getattr(T, 'id') == id).one()
