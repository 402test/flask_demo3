import re
dic = {
    'email':"^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$",
    'name':'^[a-zA-Z0-9_]{4,12}$',
    'password':'^[a-zA-Z0-9_\+-=]{6,18}$',
    'age':'(^[1-9][0-9]$)|(^[0-9]$)',
    'img':'^(\w){4}$'
}

def v_field(**fields):
    print(fields)
    # 字段验证 接受键值对
    for k,v in fields.items():
        if k in dic:
            print(k,v)
            if not v:
                return 'error'
            res = re.findall(dic[k],v)
            if not res:
                return 'error'
    else:
        return 'ok'

