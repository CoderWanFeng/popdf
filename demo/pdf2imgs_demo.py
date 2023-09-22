# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站 ：www.python-office.com
@Date    ：2023/5/30 22:30 
@Description     ：
'''
import popdf

pdf_path = r'D:\workplace\code\github\popdf\tests\test_files\pdf'
output_path = r'./output'
popdf.pdf2imgs(pdf_path, output_path, merge=True)
