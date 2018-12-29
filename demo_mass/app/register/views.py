from flask import  render_template, request, session
from ..tool.random_active_code import get_active_code
from ..tool.send_email import Mail
from ..tool.verification_field import v_field
from . import register
from ..models import *

@register.route('/register',methods=['GET','POST'])
def register_views():
    if request.method =='GET':
        return render_template('register.html')
    else:
        # 接受注册页面传递的参数
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        sex = request.form.get('sex')
        age = request.form.get('age')

        #  可能出现 不通过前端页面来访问服务器 -- 后台再次验证数据
        ver = v_field(email=email, name=name, password=password, age=age,img = request.form.get('img'))
        if ver =='error':
            return '服务器崩溃'
        #  先验证验证码是否正确
        if request.form.get('img').lower() != session.get('img').lower():
            print(request.form.get('img'))
            print(session.get('img'))
            #del session['img']
            return render_template('register.html', error='验证码错误')
        print('验证成功')

        # 判断邮箱是否已存在并激活  则返回 邮箱已经生效,无需再注册
        un_email = db.session.query(User).filter(User.email==email ,User.active_code==1).first()
        if un_email:
            return render_template('register.html', error='此邮箱已经存在')
        #  如果存在,但是没有激活,就删除之前的记录,再重新发送
        un_email_t = db.session.query(User).filter(User.email==email ,User.active_code==0).first()
        if un_email_t:
            db.session.delete(un_email_t)

        #  再发送邮件
        active_code = get_active_code()  # 生成随机链接
        send_email_state = Mail(email, '139.199.28.199:8080/vetify/%s' % active_code)
        f_t_send = send_email_state.send()
        print(locals())
        #  如果不存在,就插入新的
        #  存库
        #          获取最后一位用户的user_id
        if not f_t_send:
            return render_template('register.html', error='邮件发送失败')
        u_id = db.session.query(User).order_by('id DESC').limit(1)
        user_id = u_id.first().user_id+1

        #  插入
        user = User(user_id,name,password,age,sex,email,active_code)
        db.session.add(user)


        return render_template('register.html',msg='邮件已发送到你的邮箱,请查看邮箱验证验证')