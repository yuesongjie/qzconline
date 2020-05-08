'''
@author: Yue Songjie
@time: 2020-05-06
'''
import unittest
import HTMLTestRunner
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from interface import back
from interface import user
from runcase.postEmail import send


class TestQzcUser(unittest.TestCase):

    def setUp(self):
        print('Test User Start')

    def test_user_chat(self):
        user.chat()

    def test_user_add(self):
        user.add()

    def test_user_comment(self):
        user.comment()

    def tearDown(self):
        pass


class TestQzcServer(unittest.TestCase):

    def setUp(self):
        print('Test Back Start')

    def test_back_add(self):
        back.add()

    def test_back_chat(self):
        back.chat()

    def test_back_open(self):
        back.strategy_open()

    def test_back_close(self):
        back.strategy_close()

    def test_back_live(self):
        link = back.live()
        print(link)
        return link

    def tearDown(self):
        pass


if __name__ == '__main__':
    report = os.getcwd() + '/report.html'

    with open(report, 'wb') as f:
        testunit = unittest.TestSuite()
        testunit.addTest(unittest.makeSuite(TestQzcUser))
        testunit.addTest(unittest.makeSuite(TestQzcServer))
        runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title='七指禅自动化测试报告' + '\n' + 'From：Yue Songjie',
                                               description='七指禅社区版线上主流程回测')
        runner.run(testunit)
        f.close()
        try:
            send()
            print('邮件发送成功')
        except:
            print('邮件发送失败')
        finally:
            pass
