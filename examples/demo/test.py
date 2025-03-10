# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：http://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/4/3 23:05 
@Description     ：
'''
# pip install python-office
import office

office.pdf.encrypt4pdf(path=r'D:\程序员晚枫的文件夹\input_pdf',
                       password='程序员晚枫的密码',
                       output_path=r'D:\程序员晚枫的文件夹\output_pdf')
