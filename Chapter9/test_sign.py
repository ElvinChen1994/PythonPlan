# -*- coding:utf-8 -*-
# @Time: 2021/9/30 下午8:13
# @Author: Elvin
import hashlib

def sign_demo(body, apikey="12456"):
    #列表生成式
    passw = ["".join(i) for i in body.items() if i[1] != "sign"]
    print(passw)
    # 参数名ASCII码从小到大排序
    passW = "".join(sorted(passw))

    strsign = passW + apikey

    def md5_pass(src):
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()

    sign = md5_pass(strsign.lower())
   # print(sign)
    body["sign"] = sign
    return body


if __name__ == '__main__':
    apikey = "123456"

    body = {
        "username":"test",
        "password":"123456",
        "mail":"",
        "sign":""
        }
    print(sign_demo(body, apikey="123456"))



