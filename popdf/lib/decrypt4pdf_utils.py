# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：wfdev7
@代码日期    ：2025/7/26 15:52 
@本段代码的视频说明     ：
'''
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter
from loguru import logger
from pofile import get_files, mkdir


def encrypt_batch_pdf(input_path, output_path, password):
    """
    批量加密PDF文件。

    :param input_path: str, 需要加密的PDF文件所在目录路径
    :param output_path: str, 加密后PDF文件保存的目录路径
    :param password: str, 用于加密PDF文件的密码
    :return: None
    """
    pdf_files = get_files(path=input_path, suffix='.pdf')
    if pdf_files == None:
        logger.error("没有找到PDF文件")
        return
    if output_path != None:
        mkdir(output_path)
    else:
        output_path = input_path
    output_path = Path(output_path).absolute()
    for pdf_f in pdf_files:
        with open(pdf_f, 'rb') as file:
            reader = PdfReader(file)

            # 创建一个PdfFileWriter对象
            writer = PdfWriter()

            # 将每一页加入到writer中
            for page in range(len(reader.pages)):
                writer.add_page(reader.pages[page])

            # 加密PDF
            writer.encrypt(password)
            # 写入加密后的PDF
            out_pdf = output_path / Path(pdf_f).name
            with open(out_pdf, 'wb') as out:
                writer.write(out)
            writer.close()


def encrypt_single_pdf(input_file, output_file, password):
    """
    对单个PDF文件进行加密处理。

    :param input_file: str, 需要加密的PDF文件路径
    :param output_file: str, 加密后保存的PDF文件路径
    :param password: str, 用于加密PDF文件的密码
    :return: None
    """
    if output_file == None:
        logger.error("请填写输出文件名和路径")
    else:
        output_file = Path(output_file).absolute()
        with open(input_file, 'rb') as file:
            reader = PdfReader(file)

            # 创建一个PdfFileWriter对象
            writer = PdfWriter()

            # 将每一页加入到writer中
            for page in range(len(reader.pages)):
                writer.add_page(reader.pages[page])

            # 加密PDF
            writer.encrypt(password)
            # 写入加密后的PDF
            with open(output_file, 'wb') as out:
                writer.write(out)
            writer.close()
