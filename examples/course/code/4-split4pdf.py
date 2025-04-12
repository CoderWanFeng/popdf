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
import os

# 当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.abspath(os.path.join(base_dir, '..', '..', '..', 'tests', 'test_files', 'pdf', '程序员晚枫.pdf'))
output_file = os.path.abspath(os.path.join(base_dir, '..', '..', '..', 'tests', 'test_files', 'pdf', 'split4pdf.pdf'))


# 截取单个PDF
popdf.split4pdf(
            input_file=input_file,
            output_file=output_file,
            from_page=1,
            to_page=1,
        )

# 拼接相对路径到绝对路径
input_path = os.path.abspath(os.path.join(base_dir, '..', '..', '..', 'tests', 'test_files', 'pdf'))
output_path = input_path

# 批量截取PDF
popdf.split4pdf(
    input_path=input_path,
    output_path=output_path,
    from_page=1,
    to_page=1,
)

"""

#### 参数说明
文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/

- input_path：输入PDF的路径一般用于批量操作
- output_path：输出PDF的路径，一般用于批量操作
- input_file: 输入PDF的文件名，可以包含路径，一般用于单个文件的操作
- output_file：输出结果的文件名，可以包含路径，一般用于单个文件的操作
- from_page: 想要截取的起始页 从1开始数
- to_page:   想要截取的结束页 从1开始数

"""

