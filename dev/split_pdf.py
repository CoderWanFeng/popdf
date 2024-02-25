# -*- coding: UTF-8 -*-
'''
@学习网站      ：www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/2/25 18:06 
@本段代码的视频说明     ：
'''

# pip install popdf
import popdf

popdf.split4pdf(input_path=r'D:\程序员晚枫的文件夹\原始.pdf',
                output_path=r'D:\程序员晚枫的文件夹\切割后的.pdf',
                from_page=0, to_page=4)
