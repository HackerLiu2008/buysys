

from email.header import Header
from email.mime.image import MIMEImage
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

# 用什么邮箱发
my_sender = "3223750580@qq.com"

# 发送给谁
send_her = "2404052713@qq.com"

# 密钥
s_keys = "hmfsyounyuutcidj"

s_2 = "avjubvfehybzcifg"

# 要发送的内容
context = "客户: 刘 。于2019/10/28 12:23:33, 在线申请充值500美元。"

# 邮件头部信息
header_info = "全球付"


def mail():
    ret = True
    try:
        msg = MIMEText(context, 'plain', 'utf-8')
        msg['From'] = my_sender
        msg['TO'] = send_her
        msg['Subject'] = Header(header_info, 'utf-8')

        server = SMTP_SSL('smtp.qq.com', 465)
        server.login(my_sender, s_2)
        server.sendmail(my_sender, send_her, msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
        ret = False
    return ret

mail()