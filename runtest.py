#!/usr/bin/env python
# _*_ coding:utf-8 _*_



import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest,time
from lib.newReport import new_report
from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner import SMTP
from config import setting
import configparser



def add_case(test_path=setting.TEST_CASE):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*API.py')
    return discover

def run_case(all_case,result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""

    # 初始化接口测试数据
    #test_data.init_data()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =  result_path + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp, title='成熟度问卷调查测试报告',description='Version 1测试结果')
    runner.run(all_case)
    fp.close()
    report = new_report(setting.TEST_REPORT) #调用模块生成最新的报告
    con = configparser.ConfigParser()
    con.read(setting.TEST_CONFIG, encoding ='utf-8')
    # --------- 读取config.ini配置文件 ---------------
    HOST = con.get("user","HOST_SERVER")
    SENDER = con.get("user","FROM")
    RECEIVER = con.get("user","TO")
    USER = con.get("user","user")
    PWD = con.get("user","password")
    SUBJECT = con.get("user","SUBJECT")
    smtp = SMTP(user=SENDER, password=PWD, host=HOST)
    smtp.sender(to=RECEIVER, attachments= filename)
    # send_email(report) #调用发送邮件模块

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)


