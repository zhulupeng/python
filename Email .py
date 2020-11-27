#coding = utf - 8
import smtplib
from email.mime.text import MIMEText
msg_from = '1754142497@qq.com'
password = "ghbotrghnafodfdh"
msg_to = '57820048@qq.com'

subject = "朱路鹏的第一次作业"
content = "手机内网：10.133.88.138；手机外网IP：172.69.35.122；wifi内网IP：10.128.81.80；wifi外网IP是：39.129.40.47"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['to'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,password)
    s.sendmail(msg_from,msg_to,msg.as_string())
    print("发送成功")
except(s.SMTPException,e):
    print("发送失败")
finally:
    s.quit()

