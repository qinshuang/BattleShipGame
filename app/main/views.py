#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2018/10/15
"""

from . import main


@main.route('/', methods=['GET', 'POST'])
# 不同的蓝本装饰器不同
def index():
    pass
