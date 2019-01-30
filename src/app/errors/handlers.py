#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: handlers.py
@time: 2019/01/30
"""

from werkzeug.exceptions import NotFound
from app.apiv1 import api

class RequestParmsError(Exception):
    pass


class DuplicateDataError(Exception):
    pass


class NoPermissionError(Exception):
    pass


@api.errorhandler(NotFound)
def not_found_error(error):
    return {"message": "Error 404"}, 404


@api.errorhandler(RequestParmsError)
def request_parms_error(error):
    return {"message": "RequestParmsError"}, 500


@api.errorhandler(DuplicateDataError)
def duplicate_data_error(error):
    return {"message": "DuplicateDataError"}, 500


@api.errorhandler(NoPermissionError)
def no_permission_error(error):
    return {"message": "NoPermissionError"}, 500
