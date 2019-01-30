#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:sqin
@file: views.py
@time: 2019/01/29
"""

from . import ns
from .serialize import *
from flask_restplus import Resource, reqparse,fields
from flask_jwt_extended import jwt_required, create_access_token,get_current_user
from .models import *
from app.commons.decorators import roles_required

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
        return {
            'message': 'User {} was created'.format(args['username']),
            'access_token': access_token
        }


role_parser = reqparse.RequestParser()
role_parser.add_argument('rolename', type=str, help='rolename')


@ns.route("/role/")
class RolesManage(Resource):

    @ns.doc("GET Role List")
    @ns.response(200, 'Success')
    @ns.marshal_with(role_schema)
    def get(self):
        return Role.get_all()
        # return RoleSchema().dump(data, many=True)

    @ns.doc("Create Role")
    @ns.expect(role_parser)
    @ns.response(201, 'Success')
    @ns.response(400, 'Validation Error')
    @ns.marshal_with(role_schema)
    def post(self):
        args = role_parser.parse_args()
        rolename = args.get("rolename")
        return Role.create_one({"name": rolename}), 201
#
#
# @ns.route("/role/<int:id>")
# class OneRoleManage(Resource):
#
#     def get(self, id):
#
#         return self.obj.get_one(id)
#
#     def delete(self, id):
#         return self.obj.delete(id)
#
#
# user_parser = reqparse.RequestParser()
# user_parser.add_argument('username', type=str, help='username', required=True)
# user_parser.add_argument('email', type=str, help='email', required=True)
# user_parser.add_argument('first_name', type=str, help='first_name', required=True)
# user_parser.add_argument('last_name', type=str, help='last_name', required=True)
#
#
# @ns.route("/user")
# class UserManage(Resource):
#     obj = UserDao()
#
#     def get(self):
#         ret = UserSchema().dump(User.get_all(), many=True)
#         return ret.data
#
#     @jwt_required
#     @roles_required("SuperAdmin")
#     def post(self):
#         args = user_parser.parse_args()
#         username = args.get("username")
#         email = args.get("email")
#         first_name = args.get("first_name")
#         last_name = args.get("last_name")
#         return self.obj.create_one({"username": username,
#                                     "email": email,
#                                     "first_name": first_name,
#                                     "last_name": last_name,
#                                     "active": True,
#                                     "password": "123456"})
#
#
# user_role_parser = reqparse.RequestParser()
# user_role_parser.add_argument('username', type=str, help='username', required=True)
# user_role_parser.add_argument('rolename', type=str, help='rolename', required=True)
#
#
# @ns.route("/user-role")
# class UserRoleManage(Resource):
#
#     def post(self):
#         args = user_role_parser.parse_args()
#         username = args.get("username")
#         rolename = args.get("rolename")
#         User.update_roles(username, rolename)
#         return {"msg": "Update Success"}