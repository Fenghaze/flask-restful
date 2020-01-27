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