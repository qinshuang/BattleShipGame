#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2019/01/29
"""

# from . import ns
from .serialize import *
from flask_restplus import Resource, reqparse, fields
from flask_jwt_extended import jwt_required, create_access_token, get_current_user
from .models import *
from app.commons.decorators import roles_required
import logging

logger=logging.getLogger(__name__)

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, help='user name', required=True)


@ns.route("/login")
class UserLogin(Resource):
    @ns.doc("Login Interface")
    @ns.expect(login_parser)
    @ns.response(400, 'Validation Error')
    @ns.response(200, 'Success')
    def post(self):
        args = login_parser.parse_args()

        #     user = User.find_by_openid(args['openid'])
        #     if not user:
        #         User(username=args['openid'], email='', openid=args['openid']).save_to_db()
        access_token = create_access_token(identity=args['username'])
        user = get_current_user()
        logger.info("{username} login success".format(username=args["username"]))
        return {
            'message': 'User {} was created'.format(args['username']),
            'access_token': access_token
        }


role_parser = reqparse.RequestParser()
role_parser.add_argument('rolename', type=str, help='rolename')


@ns.route("/role/")
class RolesManage(Resource):

    @ns.doc("GET Role List")
    @ns.marshal_with(role_schema)
    @ns.response(200, 'Success')
    def get(self):
        return Role.get_all()

    @ns.doc("Create Role")
    @ns.expect(role_parser)
    @ns.marshal_with(role_schema)
    @ns.response(201, 'Success')
    @ns.response(400, 'Validation Error')
    def post(self):
        args = role_parser.parse_args()
        rolename = args.get("rolename")
        return Role.create_one({"name": rolename}), 201


#
#
@ns.route("/role/<int:id>")
class OneRoleManage(Resource):

    @ns.doc("GET A Role Detail")
    @ns.marshal_with(role_schema)
    @ns.response(200, 'Success')
    def get(self, id):
        return Role.get_one(id)

    @ns.doc("Delete A Role ")
    @ns.marshal_with(role_schema)
    @ns.response(200, 'Success')
    def delete(self, id):
        return Role.delete(id)


user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, help='username', required=True)
user_parser.add_argument('email', type=str, help='email', required=True)
user_parser.add_argument('first_name', type=str, help='first_name', required=True)
user_parser.add_argument('last_name', type=str, help='last_name', required=True)


#
@ns.route("/user")
class UserManage(Resource):

    @ns.doc("GET Users List")
    @ns.marshal_with(user_schema)
    @ns.response(200, 'Success')
    def get(self):
        return User.get_all()

    @ns.doc("Create A User")
    @ns.expect(user_parser)
    @ns.marshal_with(user_schema)
    @ns.response(200, 'Success')
    # @jwt_required
    # @roles_required("SuperAdmin")
    def post(self):
        args = user_parser.parse_args()
        username = args.get("username")
        email = args.get("email")
        first_name = args.get("first_name")
        last_name = args.get("last_name")
        return User.create_one({"username": username,
                                "email": email,
                                "first_name": first_name,
                                "last_name": last_name,
                                "active": True,
                                "password": "123456"}), 201


user_role_parser = reqparse.RequestParser()
user_role_parser.add_argument('username', type=str, help='username', required=True)
user_role_parser.add_argument('rolename', type=str, help='rolename', required=True)


@ns.route("/user-role")
class UserRoleManage(Resource):

    @ns.doc("A User set roles")
    @ns.expect(user_role_parser)
    @ns.response(200, 'Success')
    @jwt_required
    @roles_required("SuperAdmin")
    def post(self):
        args = user_role_parser.parse_args()
        username = args.get("username")
        rolename = args.get("rolename")
        User.update_roles(username, rolename)
        return {"msg": "Update Success"}

