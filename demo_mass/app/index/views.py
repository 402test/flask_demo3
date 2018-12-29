from flask import session, render_template, url_for, redirect, request, make_response
import time
from . import index
from ..models import *
import math

@index.route('/<int:page>')
@index.route('/')
def index_int_view(page=0):
    '''
    首页视图
    :param page:页数
    :return:index.html
    '''

    if page>1000:
        return '服务器崩溃'
    messages = Message.query.filter().order_by(Message.m_id.desc()).slice(page*5,(page+1)*5)
    nums =  len(Message.query.filter().all())
    all_pages = math.ceil(nums/5)
    print(messages)
    u_name = None
    next = page+1 if page+1<all_pages else None
    previous = str(page-1) if page>=1 else None
    if 'email' in session: # 如果已经登录  则页面显示用户名
        user = User.query.filter(User.email==session['email']).first()
        u_name = user.name
    if page == 0:
        page=-1  #  当 第一页的时候  没有上一页的标签  所有少算一个  结合前端的代码 用做显示当前页数
    return render_template('index.html',name = u_name,\
                           messages = messages , all_pages=all_pages,next = next,previous = previous,page = page)




    #return redirect(url_for('.index_int_view',page=0))  #可以重定向
    #  或者再写一遍
    # messages = Message.query.filter().limit(5)
    # return render_template('index.html', messages=messages)



@index.route('/add')
def add_views():
    res = '添加留言成功'
    if 'email' not in  session:
        res = '请先登录'
        return res
    else:
        texts = request.args.get('mytext')
        print(texts)  #  获取留言
        if not texts:
            return '不能为空'
        email = session['email']
        user = User.query.filter(User.email==email).first() #  用户
        u_id = user.id
        get_m_id =  db.session.query(Message).order_by('m_id DESC').limit(1).first()
        m_id = get_m_id.m_id+1  #  新增留言的m_id
        message = Message(m_id,texts,u_id,time.strftime("%Y-%m-%d %H:%I:%S", time.localtime( time.time() ) ) )
        db.session.add(message)

        return res
# -------------------------------------------------------

#    重定向传参  还没有解决
    # 先验证身份
    # res = make_response()
    # if not request.session['email']:
    #     return '服务器崩溃'



@index.route('/test')
def test_index():
    user =  User.query.filter(User.id==1).first()
    print(user.messages.all())
    return 'ok'