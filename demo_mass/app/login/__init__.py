#login目录：包含主要业务逻辑的路由和视图
from flask import Blueprint
login = Blueprint('login',__name__)

from . import views