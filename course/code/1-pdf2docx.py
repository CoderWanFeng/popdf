# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2025/1/20 21:56
@本段代码的视频说明     ：
'''
# pip install popdf

import popdf

popdf.pdf2docx(
    input_file=r'./test_files/pdf/程序员晚枫.pdf',
    output_path=r'./test_files/doc/'
)

# import poword
#
# poword.docx2pdf(
#     path='./test_files/docx/程序员晚枫.docx',
#     output_path='./test_files/test/'
# )

"""
#### 参数说明
文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/

- input_path：输入PDF的路径一般用于批量操作
- output_path：输出PDF的路径，一般用于批量操作
- input_file: 输入PDF的文件名，可以包含路径，一般用于单个文件的操作
- output_file：输出结果的文件名，可以包含路径，一般用于单个文件的操作
- input_file_list: 输入PDF的文件列表，一般用于批量操作，例如：合并2个pdf文件
"""
