"""
如果不使用flask-restful，则使用如下代码（普通的路由方式）
"""
#from app.resources import main
# @main.route('/')
# def hello_world():
#     return 'Hello World!'

from flask_restful import Resource
from .parsers import parser

class TODO(Resource):
    def get(self):
        req = parser.parse_args()
        id = req['id']
        return {'id': id}

