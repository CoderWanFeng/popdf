# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/8/4 2:25 
@本段代码的视频说明     ：
'''
import PyPDF2


def count_pdf_pages(pdf_file_path):
    """
    计算给定PDF文件的页数。

    :param pdf_file_path: PDF文件的路径
    :return: 文件的页数
    """
    try:
        with open(pdf_file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            page_count = len(reader.pages)
            return page_count
    except FileNotFoundError:
        print(f"文件未找到: {pdf_file_path}")
    except Exception as e:
        print(f"处理文件时发生错误: {pdf_file_path}, 错误详情: {e}")


# 替换这里的路径为你想要统计页数的PDF文件路径
pdf_file_path = r'D:\workplace\code\github\popdf\tests\test_files\pdf/merge.pdf'

page_count = count_pdf_pages(pdf_file_path)
if page_count is not None:
    print(f"PDF文件 '{pdf_file_path}' 的页数为: {page_count}")
