#coding=utf-8


import smtplib    #引入SMTP协议包
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #创建包含多个部分的邮件体
from email.mime.image import MIMEImage


msg_to = "2404052713@qq.com"  # 收件人邮箱


def send(context, pci_name, msg_to):
    msg_from = "3223750580@qq.com"  # 发送方邮箱
    passwd = "avjubvfehybzcifg"  # 填入发送方邮箱的授权码
    subject = "全球付"  # 主题
    msg = MIMEMultipart('related')
    content = MIMEText('<html><body><div>' + context + '</div><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
    # msg = MIMEText(content)
    msg.attach(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    file = open(msg_to, "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    msg.attach(img)

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except Exception as e:
        print(str(e))

