#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: __init__.py
@time: 2018/10/15
"""

from flask import Flask
from flask_restplus import marshal
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
import json

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 可以直接把对象里面的配置数据转换到app.config里面
    config[config_name].init_app(app)
    jwt = JWTManager(app)
    db.init_app(app)

    # 路由和其他处理程序定义
    # ...
    # from .main import main as main_blueprint  # 从当前目录下面的main子目录导入main
    from .apiv1 import apiv1_blueprint
    # app.register_blueprint(main_blueprint)
    app.register_blueprint(apiv1_blueprint, url_prefix="/api/v1")

    from app.apiv1.users.serialize import user_schema
    from app.apiv1.users.models import User

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        return json.dumps(marshal(User.get_by_username(identity), user_schema))

    return app
