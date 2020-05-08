'''
@author: Yue Songjie
@time: 2020-05-06
'''
import requests as rq
from common import funct as cf, constant
import json

token = cf.get_token_user()
headers = {'Token': token}


# 评论
def comment():
    url_list = constant.url + '/api/v4/home/feed?roomId=105&sinceTime=null&sort='
    url_detail = constant.url + '/api/v4/post-comment/add-comment'
    r1 = rq.post(url=url_list, headers=headers).text
    oid = json.loads(r1)['data']['feedList'][0]['show']['oid']
    time = cf.otherStyleTime()
    data = {
        'PostChatId': oid,
        'content': '评论' + time,
        'type': '2',
        'roomId': '105'
    }
    r = rq.post(headers=headers, url=url_detail, data=data).text
    assert json.loads(r)['code'] == 200


# 讨论区
def chat():
    time = cf.otherStyleTime()
    url = constant.url + '/api/v1/chat/post'
    data = {
        'roomId': '105',
        'chatContent': '大家好' + time
    }
    r = rq.post(url=url, data=data, headers=headers).text
    assert json.loads(r)['code'] == 200


# 发帖
def add():
    url = constant.url + '/api/v4/post/add'
    data = {
        'roomId': '105',
        'content': '测试' + cf.otherStyleTime(),
        'push': '0'
    }
    r = rq.post(url=url, data=data, headers=headers).text
    assert json.loads(r)['code'] == 200


comment()
