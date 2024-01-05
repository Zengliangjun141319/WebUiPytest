# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sendemail.py
   Description :   通过smtplib\email库来发送邮件
   Author :        曾良均
   QQ:             277099728
   Date：          9/13/2021 8:59 AM
-------------------------------------------------
   Change Activity:
                   9/13/2021: add
                   9/28/2021: 增加异常信息输出
-------------------------------------------------
"""
__author__ = 'ljzeng'

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email import encoders
from selenium import webdriver
import time
import os
from datetime import datetime
from logger import Log
from selenium.webdriver.chrome.options import Options

log = Log()
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

log.logname = 'sendmail.log'


def reportScreenshot(report):
    # 打开报告
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    reportpath = r'file:///' + os.path.join(BASE_DIR, report)
    # 设置Chrome为‘无界面模式',便于全屏截长图
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chdriver = webdriver.Chrome(options=chrome_options)
    chdriver.get(reportpath)
    chdriver.implicitly_wait(60)
    time.sleep(3)
    #  获取页面的宽、高
    w = chdriver.execute_script("return document.documentElement.scrollWidth")
    h = chdriver.execute_script("return document.documentElement.scrollHeight")
    chdriver.set_window_size(width=w, height=h)

    try:
        log.info("open report, and screenshot.")
        chdriver.save_screenshot('.\\report\\report.png')
        time.sleep(2)
    except:
        print("Screenshot fail")
        log.info("Screenshot fail")
    chdriver.quit()


def sendEmail(ver, report, runtime):
    # 发件人
    senders = [['xiaoer-82@tom.com', 'Xiaoer1982-', 'smtp.tom.com', 'Tom邮箱'],
               ['xiaoer_82@sina.cn', 'Xiaoer1982-', 'smtp.sina.com', '新浪邮箱']]

    # 收件人
    receivers = ['LJZeng@foresightintelligence.com', 'LWang@foresightintelligence.com', 'llj@foresightintelligence.com', 'xiongdh79@126.com']   # 可设置多个收件人
    cc = ['QHong@foresightintelligence.com', 'DCHu@foresightintelligence.com', 'zljun8210@163.com']
    # receivers = ['LJZeng@foresightintelligence.com']
    # cc = ['zljun8210@163.com']

    # 邮件内容设置
    mail_msg = r"""
    <!DOCTYPE html>    
<html>    
<head>    
<meta charset="UTF-8">    
</head>    
    
<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"    
    offset="0">    
    <table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">    
        <tr>    
            本邮件由系统自动发出，无需回复！<br/>            
            大家好，以下是 IronIntel 项目自动化测试执行信息</br> 
            <br />
            <td><font color="#2000FF">执行信息 </font>  
            <hr size="2" width="100%" align="left" /></td>  
        </tr>
        <tr>    
            <td>    
                <ul>    
                    <li>项目名称 ： IronIntel</li>
                    <li>测试版本 ： {version}</li>    
                    <li>执行时间 ： {runtime}</li>    
                    <li>触发原因： 版本升级</li>
                </ul>
            </td>    
        </tr>     
        <tr>    
            <td><br />    
            <b><font color="#0B610B">执行结果</font></b>    
            <td />
        </tr>
        <tr><br /></tr>    
        <tr>    
            <td><img src="cid:image"></td>  
        </tr>    
    </table>    
</body>    
</html>
    """

    # 配置多个发件箱，当发送失败时，使用下一组发件箱配置
    for ser in senders:
        sender = ser[0]
        sendPass = ser[1]
        server = ser[2]
        name = ser[3]

        message = MIMEMultipart()
        subject = '%s 版本自动化测试结果' % ver
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = sender
        message['To'] = ";".join(receivers)
        message['Cc'] = ";".join(cc)
        # 邮件正文
        mail_msg = mail_msg.format(version=ver, runtime=runtime)
        message.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        # 报告截图
        try:
            # 打开报告并截图
            reportScreenshot(report)
            time.sleep(3)
            fp = open('.\\report\\report.png', 'rb')
            messageImage = MIMEImage(fp.read())
            fp.close()
            messageImage.add_header('Content-ID', '<image>')
            message.attach(messageImage)
            log.info("get test report screenshot")
            os.system("del .\\report\\report.png")
        except Exception as e:
            messageImage = None
            messageImage.add_header('Content-ID', '<image>')
            message.attach(messageImage)
            log.info(e.args)
            log.info("Failed to get screenshot!")

        # 邮件附件
        try:
            attRe = MIMEText(open(report, 'rb').read(), 'html', 'utf-8')
            attRe["Content-Type"] = 'text/html'
            # 中文附件名处理方式
            attRe.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '%s 版本测试报告.html' % ver))
            encoders.encode_base64(attRe)
            message.attach(attRe)
            time.sleep(3)
            log.info("Attachment loaded successfully！！")
        except Exception as e:
            log.info(e.args)
            log.info("Attachment loaded failer!")

        # 发送邮件
        try:
            # ser = smtplib.SMTP_PORT(server, port)   # 发件人邮箱的SMTP服务器，端口
            ser = smtplib.SMTP(server)
            ser.login(sender, sendPass)    # 发件人账号，密码
            ser.sendmail(sender, receivers + cc, message.as_string())    # 发件人邮箱、收件人邮箱、邮件内容
            time.sleep(5)
            ser.quit()    # 关闭连接
        except Exception as e:
            log.info(e.args)
            log.info("%s: Failed to send mail" % name)
            continue
        else:
            log.info("%s: Mail sent successfully！！" % name)
            break


if __name__ == '__main__':
    nowtime = datetime.now().strftime("%Y.%m.%d %H:%M")
    version = '2.21.908'
    reoprtf = r'./report/result_2022.06.27.162346.843.html'
    sendEmail(version, reoprtf, runtime=nowtime)
