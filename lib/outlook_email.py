
import win32com.client as win32
import datetime, os
 
addressee = 'zhangnan@haier.com'
#addressee = 'zhangnan@haier.com'+';'+'zhangyang.cosmo@haier.com'#收件人邮箱列表
#cc = 'test02@163.com'+';'+'test03@alibaba.com'#抄送人邮件列表
mail_path = os.path.join(r'E:\work\自动化测试\interface_testing\report', '2020-12-30 16_50_14result.html')#获取测试报告路径
 
# class send_email(self, file_new):
#     def outlook(self, file_new):
#         olook = win32.Dispatch("outlook.Application")
#         mail = olook.CreateItem(0)
#         #mail = olook.CreateItem(win32.constants.olMailItem)
#         mail.To = addressee#收件人
#         #mail.CC = cc#抄送人
#         # mail.Recipients.Add(addressee)
#         mail.Subject = str(datetime.datetime.now())[0:19]+'just a testing'#邮件主题
#         mail.Attachments.Add(file_new, 1, 1, "myFile")
#         read = open(file_new,"r",encoding='utf-8')#打开需要发送的测试报告附件文件
#         content = read.read()
#         #content = read.read().decode('gb2312').encode('utf-8')#读取测试报告文件中的内容
#         read.close()
#         mail.HTMLBody = content
#         #mail.Body = content#将从报告中读取的内容，作为邮件正文中的内容
#         #mail.Display() # 这一步非常重要，没了这一步，在网页版邮箱就无法显示图片
#         mail.Send()#发送

def send_email(file_new):
    olook = win32.Dispatch("outlook.Application")
    mail = olook.CreateItem(0)
    #mail = olook.CreateItem(win32.constants.olMailItem)
    mail.To = addressee#收件人
    #mail.CC = cc#抄送人
    # mail.Recipients.Add(addressee)
    mail.Subject = str(datetime.datetime.now())[0:19]+'automation testing report'#邮件主题
    mail.Attachments.Add(file_new, 1, 1, "myFile")
    read = open(file_new,"r",encoding='utf-8')#打开需要发送的测试报告附件文件
    content = read.read()
    #content = read.read().decode('gb2312').encode('utf-8')#读取测试报告文件中的内容
    read.close()
    mail.HTMLBody = content
    #mail.Body = content#将从报告中读取的内容，作为邮件正文中的内容
    mail.Display() # 这一步非常重要，没了这一步，在网页版邮箱就无法显示图片
    mail.Send()#发送
 
 
if __name__ == '__main__':
    file_new = os.path.join(r'E:\work\自动化测试\interface_testing\report', '2020-12-30 16_50_14result.html')
    send_email(file_new)

