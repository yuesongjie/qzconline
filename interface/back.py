'''
@author: Yue Songjie
@time: 2020-05-06
'''
import requests as rq
from common import funct as cf, constant
import json

token = cf.get_token()  # 登录


# 开仓晒单
def strategy_open():
    url = constant.url + '/api/v4/post/strategy-open'
    headers = {
        'Token': token
    }
    data = {
        'cost': '20840.0',
        'LossPrice': '2000',
        'margin': '2294.6',
        'name': '玉米2009',
        'num': 1,
        'openImg': constant.openImg,
        'openPrice': '2086.00',
        'openReason': '测试',
        'openTime': '2020-05-06 14:53:56',
        'profitPrice': '2999',
        'roomId': '105',
        'shareRoomIds': '105',
        'symbol': 'c2009',
        'type': '1'
    }
    r = rq.post(url=url, headers=headers, data=data).text
    msg = json.loads(r)['msg']
    # time.sleep(60)
    assert msg == '发帖成功' or '操作太快'


def strategy_close():
    url_list = constant.url + '/api/v4/post/strategy-symbol?roomId=105&symbol=c2009&type=1'
    headers = {'Token': token}
    r_list = rq.post(url=url_list, headers=headers).text
    if r_list is not None:
        iD = json.loads(r_list)['data']['openList'][0]['strategyId']
    url = constant.url + '/api/v4/post/strategy-close'
    data = {
        'closeImg': constant.closeImg,
        'closePrice': '2085.00',
        'closeReason': '平仓晒单测试',
        'closeTime': '2020-05-06 21:29:33',
        'roomId': '105',
        'strategyId': iD
    }
    rq.post(url=url, data=data, headers=headers)
    r = rq.post(url=url, headers=headers, data=data).text
    msg = json.loads(r)['msg']
    # time.sleep(60)
    assert msg == '发帖成功' or '操作太快'


def live():
    Url = constant.url
    url_add_chat = Url + '/api/v4/chat-live/add-chat-live'  # 新增预告
    url_find = Url + '/api/v4/chat-live/chatlive-detail'  # 查看有无预告
    url_creat_live = Url + '/api/v4/chat-live/create-live'  # 新建直播
    url_del = Url + '/api/v4/chat-live/del-pre'  # 删除预告
    headers_live = {
        'token': token
    }
    data_add_chat = {
        'content': '回测',
        'type': '0',
        'roomId': '105'
    }  # 预告data
    data_find = {
        'roomId': '105'
    }  # 查看预告data
    data_creat = data_find  # 新建直播data
    r_find = rq.post(url=url_find, data=data_find, headers=headers_live).text
    d_find = json.loads(r_find)['data']  # 查看有无预告
    if d_find is not None:
        iD = d_find['id']
        data_del = {'id': iD}
        rq.post(url=url_del, data=data_del, headers=headers_live)  # 如果已存在预告则删除预告
    else:
        pass
    rq.post(url=url_add_chat, data=data_add_chat, headers=headers_live)  # 新增预告
    r_creat = rq.post(url=url_creat_live, data=data_creat, headers=headers_live).text  # 创建直播
    d_creat = json.loads(r_creat)['code']
    assert d_creat == 200
    link = json.loads(r_creat)['data']['vhallStartUrl']
    print(link)
    return link


# 发帖
def add():
    time = cf.otherStyleTime()
    headers = {'Token': token}
    url = constant.url + '/api/v4/post/add'
    data = {
        'roomId': '105',
        'content': '发帖时间：' + time,
        'image[]': constant.image,
        'push': '1'
    }
    r = rq.post(url=url, data=data, headers=headers).text
    assert json.loads(r)['code'] == 200


def chat():
    time = cf.otherStyleTime()
    url = constant.url + '/api/v1/chat/post'
    data = {
        'roomId': '105',
        'chatContent': '大家好' + time
    }
    headers = {'Token': token}
    r = rq.post(url=url, data=data, headers=headers).text
    assert json.loads(r)['code'] == 200


strategy_open()
