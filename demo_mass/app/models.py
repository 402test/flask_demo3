from . import db
class User(db.Model):
    '''
    用户表
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String)
    password = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    email = db.Column(db.Integer)
    active = db.Column(db.Integer)
    active_code = db.Column(db.String)

    messages = db.relationship('Message',backref='user',lazy = 'dynamic')

    def __init__(self,user_id,name,password,age,sex,email,active_code):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.age = age
        self.sex = sex
        self.email = email
        self.active='0'
        self.active_code = active_code

    def __repr__(self):
        return 'User %s,%s,%s,%s,%s,%s,%s'%(self.user_id,self.name,self.password,self.age\
                                            ,self.sex,self.email,self.active)
    def __str__(self):
        self.__repr__()



class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    m_id = db.Column(db.Integer)
    m_text = db.Column(db.String)
    mtime = db.Column(db.TIMESTAMP)

    #  外键关联
    u_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,m_id,m_text,u_id,mtime):
        self.m_id = m_id
        self.m_text = m_text
        self.u_id = u_id
        self.mtime = mtime

    def __str__(self):
        return 'Message %s  , %s  ,%s '%(self.m_id,self.m_text, self.u_id)


# 同步回数据库
db.create_all()

