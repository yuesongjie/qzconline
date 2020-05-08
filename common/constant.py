'''
@author: Yue Songjie
@time: 2020-05-06
'''
# url
url = 'http://www1.xiyan98.com'
url_test = 'http://139.224.196.167:13221'

login_data_test = {
    'password': '123qwe',
    'username': 'yuesongjie'
}
login_data = {
    'password': 'ysj1025',
    'username': 'yuesongjie'
}

login_data_user = {
    'password': '123qwe',
    'username': '10100229'
}
login_headers = {
    'APPVER': "1.0",
    'CHANNEL': "lanyi_ios",
    'OS': "iOS 13.4.1",
    'PL': 'IOS',
    'SIGN': '64c15e482aef198b6a7c783524795cc5',
    "User-Agent": "LyCompassForum/1.0 (iPhone; iOS 13.4.1; Scale/2.00)"
}

# desired_caps
desired_caps_iOS = {
    "platformName": "iOS",
    "platformVersion": "13.4.1",
    "deviceName": "iPhone 8 Plus",
    "udid": "bbba4cc764a7ab5138f58d8a48c248cf83b7c384",
    "noReset": True,
    "bundleId": "com.tianying.ykftox"
}
desired_caps_Android = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "HUAWEI Mate 20 Pro",
    "noReset": True,
    "appPackage": "com.yingkuan.futures",
    "appActivity": ".model.SplashActivity"
}

image = 'http://img.xidu98.com/data/live/549133a367941809d3e96a4a6faf73b7'
openImg = 'http://img.xidu98.com/data/live/db562124ec244e02c6ac11fa2173d7c8'
closeImg = 'http://img.xidu98.com/data/live/7b73681971605944f921c1d43389e7bb'
