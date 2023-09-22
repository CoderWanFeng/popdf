# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站      ：www.python-office.com
@代码日期    ：2023/7/13 22:08 
@本段代码的视频说明     ：
'''

# 导入pdfplumber
import pdfplumber

# 读取pdf文件，保存为pdf实例
pdf =  pdfplumber.open("E:\\nba.pdf")

# 访问第二页
first_page = pdf.pages[1]

# 自动读取表格信息，返回列表
table = first_page.extract_table()
