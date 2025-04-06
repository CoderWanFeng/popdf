# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2025/4/4 22:52 
@本段代码的视频说明     ：
'''
import unittest


class TestPDF(unittest.TestCase):

    def test_exception(self):
        try:
            fdas
        except Exception as e:
            print(type(e).__name__,str(e))
