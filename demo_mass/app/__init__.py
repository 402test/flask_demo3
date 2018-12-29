#对整个应用程序做初始化操作
#主要工作：
#1.创建Flask应用以及各种配置
#2.创建数据库实例-SQLAlchemy的实例
#3.通过蓝图(Blueprint)关联其他的业务程序
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import platform
pymysql.install_as_MySQLdb()
#创建数据库实例
db = SQLAlchemy()
#通过一个函数创建app
def create_app():
    app = Flask(__name__)
    if (platform.system() == 'Windows'):
        password = 'root'
    else:
        password='123456'
    #有关app的配置
    app.config['DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:%s@localhost:3306/hcw_xidu_demo_one'%password

    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 自动提交
    app.config['SECRET_KEY'] = 'suisuibianbian'  # session  key
    # 使用app初始化db(数据库实例)

    db.init_app(app)
    app.app_context().push()
    #  关联注册register
    from .register import register as register_blueprint
    app.register_blueprint(register_blueprint)
    # 关联users
    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint)

    # 关联 index

    from .index import index as index_blueprint
    app.register_blueprint(index_blueprint)

    return app