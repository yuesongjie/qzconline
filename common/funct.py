'''
@author: Yue Songjie
@time: 2020-05-06
'''
import requests as rq
from common import constant
import json
import time


def get_token():
    # envir=input('请输入运行环境：')
    # if envir=='test':
    #     Url = constant.url_test
    #     data=constant.login_data_test
    #     url = Url + '/api/v1/user/login'
    #     r = rq.post(headers=constant.login_headers, url=url, data=data).headers
    #     token = json.loads(json.dumps(dict(r)))['Token']
    # else:
    #     Url = constant.url
    #     data = constant.login_data
    #     url = Url + '/api/v1/user/login'
    #     r = rq.post(headers=constant.login_headers, url=url, data=data).headers
    #     token = json.loads(json.dumps(dict(r)))['Token']
    Url = constant.url
    data = constant.login_data
    url = Url + '/api/v1/user/login'
    r = rq.post(headers=constant.login_headers, url=url, data=data).headers
    token = json.loads(json.dumps(dict(r)))['Token']
    return token


def get_token_user():
    Url = constant.url
    data = constant.login_data_user
    url = Url + '/api/v1/user/login'
    r = rq.post(headers=constant.login_headers, url=url, data=data).headers
    token = json.loads(json.dumps(dict(r)))['Token']
    return token


def otherStyleTime():
    now = time.time()
    timeArray = time.localtime(now)
    styleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    return styleTime
