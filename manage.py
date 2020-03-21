# coding:utf-8


from ihome import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from wsgiref.simple_server import make_server


# 创建flask的应用对象
app=create_app("develop")

manager = Manager(app)
Migrate(app, db)
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    # server = make_server('127.0.0.1', 5000, app)
    # server.serve_forever()
    manager.run()