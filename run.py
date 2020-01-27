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