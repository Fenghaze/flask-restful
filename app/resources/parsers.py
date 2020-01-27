from flask_restful import reqparse

parser = reqparse.RequestParser()

# 添加参数解析
parser.add_argument('id', type=int, location='args')
