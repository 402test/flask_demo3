#login目录：包含主要业务逻辑的路由和视图
from flask import Blueprint
index = Blueprint('index',__name__)

from . import views