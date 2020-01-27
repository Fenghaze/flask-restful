<center>
    <h1>
        FLASK-API项目结构搭建
    </h1>
</center>

[@toc]

# 1 FLASK-API项目结构

- `flask-restful`：api
- `flask-script`：命令
- `flask-sqlalchemy`：数据库

![项目结构](https://github.com/Fenghaze/flask-restful/blob/master/%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84.png)

# 2 快速开始

- 安装需求文件`requirements.txt`

```
pip install -r requirements.txt
or
conda install --yes --file requirements.txt
```

- 初始化数据库命令

```
python run.py initdb
```

- 运行`run.py`

# 3 具体实现

## 3.1 根目录test

> test/config.py

```python
class Config:
    SECRET_KEY = 'key string'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/test'
    # 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名 data_base
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
```

> test/run.py

```python
import click
from app import create_app
from app.database.models import *
from flask_script import Manager
app = create_app()
manager = Manager(app)

@manager.command
def initdb():
    db.drop_all()
    db.create_all()
    click.echo('初始化数据库')

@manager.command
def insert():
    category1 = Category(name='1234')
    db.session.add(category1)
    db.session.commit()
    click.echo('添加一个类别')

if __name__ == '__main__':
    manager.run()
```

## 3.2 项目文件夹app

> test/app/\_\_init__.py

```python
from flask import Flask
from config import Config
from app.resources import main
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 函数工厂
def create_app():
    # 初始化flask
    app = Flask(__name__)
    # 从对象设置配置信息
    app.config.from_object(Config)
    # 第三方扩展初始化
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(main)
    return app
```

### 3.2.1 数据库文件夹database

> test/app/database/models.py

```python
from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
```

### 3.2.2 路由文件夹resources

> test/app/resources/_\_init__.py

```python
from flask import Blueprint
from flask_restful import Api
from app.resources.views import *

# 定义蓝图，main为蓝图名字
main = Blueprint('main', __name__)
# 实例化api
api = Api(main)

# 设置路由
api.add_resource(TODO, '/index')
```

> test/app/resources/views.py

```python
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
```

> test/app/resources/parsers.py

```python
from flask_restful import reqparse

parser = reqparse.RequestParser()

# 添加参数解析
parser.add_argument('id', type=int, location='args')

```

