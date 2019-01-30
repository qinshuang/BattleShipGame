#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: baseMixin.py
@time: 2019/01/02
"""

from app import db
from app.errors.handlers import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc, asc


class BaseMixin(object):

    def get_q(self, T):
        return db.session.query(T)

    @classmethod
    def get_all(cls, page=1, per_page=10, sortby=None, order='asc', search=None):
        """

        :param page:
        :param per_page:
        :param sortby:
        :param order:
        :param search:
        :return:
        """
        start_index = per_page * (page - 1) + 1

        query = db.session.query(cls).limit(per_page).offset(start_index)
        if sortby:
            if order == "asc":
                query = query.order_by(asc(getattr(cls, sortby)))
            else:
                query = query.order_by(desc(getattr(cls, sortby)))
        if search:
            for k, v in search.items():
                query = query.filter(getattr(cls, k).like("%{}%".format(v)))
        return query.all()

    @classmethod
    def create_one(cls, data):
        if not data:
            raise RequestParmsError
        try:
            new_t = cls(**data)
            db.session.add(new_t)
            db.session.commit()
        except IntegrityError:
            raise DuplicateDataError
        except BaseException as e:
            raise RequestParmsError
        return new_t

    @classmethod
    def get_one(cls, id):
        return db.session.query(cls).filter_by(id=id).one()

    @classmethod
    def delete(cls, id):
        data = id
        if not data:
            raise RequestParmsError
        try:
            t = db.session.query(cls).filter_by(id=id).one()
            db.session.delete(t)
            db.session.commit()
        except BaseException as e:
            raise RequestParmsError
        return True
