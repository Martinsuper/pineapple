#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "martindly@163.com"  # 用户名
mail_pass = "FOBLETDZXOOCUMIS"  # 口令

sender = 'martindly@163.com'  # 发件人邮箱(最好写全, 不然会失败)
receivers = ['582791000@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

content = '<h1>时光匆匆</h1>'
title = '匆匆'  # 邮件主题


def sendEmail():
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    sendEmail()
