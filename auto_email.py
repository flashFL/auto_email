import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import schedule
import time

def sendmail():
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = '976668382@qq.com'  # 用户名
    mail_pass = 'npstgqgglrrqbeib'  # 口令

    # sender = input('Enter mailcount')
    receivers = ['976668382@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEMultipart('related')
    message['From'] = Header("fafa", 'utf-8')
    message['To'] = Header("小可爱", 'utf-8')
    message['Subject'] = Header('Hi~ o(*￣▽￣*)ブ')

    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)


    mail_msg = '''
    <p>小可爱，下午好！</p>
    <p><img src="http://pic1.win4000.com/mobile/2018-08-17/5b769194be2e5.jpg"></p>
    <p>爱你哟</p>
    <p><a href = 'https://github.com/flashFL/auto_email'>Git主页<<<</a></p>
    '''
    message.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # 指定图片为当前目录
    fp = open('1.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')


    att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att1)

    att2 = MIMEText(open('root.txt', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="root.txt"'
    message.attach(att2)



    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def auto_email():
    schedule.every().friday.at('15:00').do(sendmail)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    sendmail()