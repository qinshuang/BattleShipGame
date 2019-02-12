#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: errorHandlers.py
@time: 2019/01/31
"""


class NoPermissionError(Exception):
    message = "No Permission Error"
    code = 403


class RequestParmsError(Exception):
    message = "Request Parms Error"
    code = 400


class DuplicateDataError(Exception):
    message = "Duplicate Data Error"
    code = 400