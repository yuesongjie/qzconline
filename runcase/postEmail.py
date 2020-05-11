from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
from bs4 import BeautifulSoup as bs
import os


def send():
    # 用户信息
    from_addr = 'yuesongjie@huashengfe.com'
    password = 'Ysj1025'  # 腾讯QQ邮箱或腾讯企业邮箱必须使用授权码进行第三方登陆
    to_addr = 'lanyi-qzc-project-list@huashengfe.com'
    # to_addr = 'yuesongjie@huashengfe.com'
    smtp_server = 'smtp.exmail.qq.com'  # 腾讯服务器地址

    report = os.getcwd() + '/report.html'
    r = open(report)
    soup = bs(r, "html.parser")

    # 内容初始化，定义内容格式（普通文本，html）
    msg = MIMEText(soup, 'HTML', 'utf-8')

    # 发件人收件人信息格式化 ，可防空
    # 固定用法不必纠结，我使用lambda表达式进行简单封装方便调用
    lam_format_addr = lambda name, addr: formataddr((Header(name, 'utf-8').encode(), addr))
    # 传入昵称和邮件地址
    msg['From'] = lam_format_addr('七指禅自动化测试', from_addr)  # 腾讯邮箱可略
    # msg['To'] = lam_format_addr('）', to_addr)  # 腾讯邮箱可略

    # 邮件标题
    msg['Subject'] = Header('七指禅线上回测结果', 'utf-8').encode()  # 腾讯邮箱略过会导致邮件被屏蔽

    # 服务端配置，账密登陆
    server = smtplib.SMTP(smtp_server, 25)

    # 登陆服务器
    server.login(from_addr, password)

    # 发送邮件及退出
    server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送地址需与登陆的邮箱一致
    server.quit()
