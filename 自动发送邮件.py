import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time

def sendmail():
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = '976668382@qq.com'  # 用户名
    mail_pass = 'ixzdeybxbvumbcge'  # 口令

    # sender = input('Enter mailcount')
    receivers = ['wangpengcheng10@huawei.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('mua!~下午好', 'plain', 'utf-8')
    message['From'] = Header("fafa", 'utf-8')
    message['To'] = Header("小可爱", 'utf-8')
    message['Subject'] = Header('Hi~ o(*￣▽￣*)ブ')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


schedule.every().friday.at('15:00').do(sendmail)

while True:
    schedule.run_pending()
    time.sleep(1)