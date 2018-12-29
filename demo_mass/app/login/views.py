from flask import  render_template, request, redirect, make_response, session
#导入蓝图程序-main，用于构建路由
from . import login
#导入db 以及　models们
#from .. import db
from ..models import *
from ..tool.get_verify_code import get_verify_code #  验证码
from io import BytesIO
from ..tool.verification_field import v_field
@login.route('/login',methods=['GET','POST'])
def login_views():
    '''
    登录视图
    :return:
    '''
    if request.method == 'GET':
        if 'email' in session:
            return redirect('/')
        else:
            if 'email' in request.cookies:
                email = request.cookies.get('email')
                session['email'] = email
                return redirect('/')
            else:
                return render_template('login.html')
    else:  #  POST
        #登录验证
        email = request.form.get('email')
        password = request.form.get('password')
        ver = v_field(email=email, password=password,  img=request.form.get('img'))
        if ver == 'error':
            return '服务器崩溃'

        if request.form.get('img').lower() != session.get('img').lower():
            #  验证码输入错误
            print(request.form.get('img'))
            print(session.get('img'))
            #del session['img']
            return render_template('login.html', error='验证码错误')

        login_vetify = User.query.filter(User.email==email).first()
        if login_vetify and login_vetify.password ==password :
            # 邮箱和密码匹配
            # 声明重定向到首页的对象
            print(login_vetify.active)
            if login_vetify.active !=1:
                return render_template('login.html', error='没有激活,请查收邮件激活,或者重新注册')
            resp = redirect('/')
            session['email'] = login_vetify.email
            if 'isSaved' in request.form:
                resp.set_cookie('email', email, 60 * 60 * 24 * 365)#  记住密码 保存cookies
            return resp
        else:
            return render_template('login.html', error='用户名或密码错误')


#   邮箱激活  访问链接之后  在数据库里面  把active 改成 1
@login.route('/vetify/<active_code>')
def vetify_email(active_code):
    updata_active  = User.query.filter(User.active_code==active_code).first()
    if updata_active:
        updata_active.active = 1
        db.session.add(updata_active)
        return '注册成功'
    else:  #  链接出错
        return 'error'

@login.route('/quit')
def quit_views():
    #  退出 删除 cookies  和 session

    if 'email' in session:
        del session['email']
        print('删除session')
    if request.cookies.get('email'):
        response = redirect('/')
        response.delete_cookie('email')
        print('删除cookie')
        return response
    return redirect('/')


@login.route('/code')  #  验证码
def code_views():
    img,code = get_verify_code()
    buf = BytesIO()
    img.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpg'
    session['img'] = code
    return response
#print(User.query.filter_by().all())
