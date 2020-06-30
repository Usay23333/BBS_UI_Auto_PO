# coding=utf-8

import smtplib, os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from utils.ConfigUtil import ConfigReader

class EmailUtil():

    def __init__(self):
        self.cr = ConfigReader()
        self.host = self.cr.get_email('server_host')
        self.port = int(self.cr.get_email('server_port'))
        self.user = self.cr.get_email('user')
        self.password = self.cr.get_email('password')
        # self.smtp = smtplib.SMTP('smtp.qq.com') # 不加密
        self.smtp = smtplib.SMTP_SSL(self.host, self.port) # SSL加密
        self.smtp.login(self.user, self.password)
        self.sender = self.user
        self.to_addrs = self.cr.get_email('to_addrs').replace('[', '').replace(']', '').replace('\'', '').replace(', ', ',').split(',')

    def send(self, title, body, file, to_addrs=None):

        message = MIMEMultipart() # 带附件的邮件
        message.attach(MIMEText(body))

        file_name = os.path.basename(file)
        fp = open(file, mode='rb')
        att = MIMEImage(fp.read()) # 图片附件
        fp.close()
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = f'attachment; filename={file_name}'
        message.attach(att)

        message['subject'] = Header(title, 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        # message['To'] = Header(str(to_addrs), 'utf-8')
        if to_addrs:
            self.to_addrs = to_addrs
        self.smtp.sendmail(self.sender, self.to_addrs, message.as_string())

        self.close()

    def send_all(self, title, body, *files, to_addrs=None):
        subject = title
        if len(files):
            message = MIMEMultipart() # 带附件的邮件
            message.attach(MIMEText(body))

            for i in files: # E:/RF_Screenshot/AjoU_2020-05-09 21-44-49.png
                if not os.path.exists(i):
                    print(f"FBI Warning!File Or Dir {i} Not Exists!!!")
                    continue
                file_name = os.path.basename(i)
                img_list = ['jpg', 'jpeg', 'png']
                print(file_name.split('.')[1])
                if file_name.split('.')[1] in img_list:
                    fp = open(i, mode='rb')
                    att = MIMEImage(fp.read())
                    fp.close()
                    att["Content-Type"] = 'application/octet-stream'
                    att["Content-Disposition"] = f'attachment; filename={file_name}'
                    message.attach(att)

        else:
            message = MIMEText(body) # 普通的文本邮件
        message['subject'] = Header(subject, 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        # message['To'] = Header(str(to_addrs), 'utf-8')
        if to_addrs:
            self.to_addrs = to_addrs
        self.smtp.sendmail(self.sender, self.to_addrs, message.as_string())

        self.close()

    def close(self):
        self.smtp.close()
if __name__ == "__main__":
    # EmailUtil().send('202005101630_zero', 'I am body', r"E:/RF_Screenshot/1.png", r"E:/RF_Screenshot/2.png")
    EmailUtil().send_all('202005101630_zero', 'I am body', r"E:/RF_Screenshot/1.png", r"E:/RF_Screenshot/2.png", to_addrs = ['568190562@qq.com'])
