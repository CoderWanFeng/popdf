# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站 ：www.python-office.com
@Date    ：2023/4/3 23:05 
@Description     ：
'''
# pip install python-office
import office

office.pdf.encrypt4pdf(path=r'D:\程序员晚枫的文件夹\input_pdf',
                       password='程序员晚枫的密码',
                       output_path=r'D:\程序员晚枫的文件夹\output_pdf')
