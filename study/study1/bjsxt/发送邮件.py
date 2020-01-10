# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.163.com"
mail_user = "asj302384cs@163.com"
mail_pass = "dgg962540"

sender = "asj302384cs@163.com"
receivers = ["ymjrchx@yeah.net"]
message = MIMEText('填写邮件内容', 'plain', 'utf-8')
message['From'] = Header('申请书', 'utf-8')
message['To'] = Header('申请', 'utf-8')
subject = '申请单志愿者'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as err:
    print("无法发送邮件：", err)

if __name__ == '__main__':
    pass
