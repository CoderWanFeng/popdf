# -*- coding: utf-8 -*-
import click
from loguru import logger

from popdf.core.Batch_PDFType import Batch_PDFType
from popdf.core.PDFType import MainPDF

mainPDF = MainPDF()
batch_main_pdf = Batch_PDFType()


@click.group()
def cli():
    logger.info("popdf 命令行工具，查看帮助：popdf --help")


@cli.command()
@click.option('--input_file', default=None)
@click.option('--output_file', default=None)
@click.option('--input_path', default=None)
@click.option('--output_path', default=None)
def pdf2docx(input_file=None, output_file=None, input_path=None, output_path=None):
    """
    PDF转Word 视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/
    > version 1.0.1
    Args:
        input_file: 输入的单个pdf的存储位置。
        output_file: 输出的单个word的存储位置，需要带后缀.docx
        input_path: 批量转换的pdf输入位置
        output_path: 批量转换后word的输出位置
    Returns:
    <= version 1.0.1
    Args:
        input_file: pdf的存储位置。
        output_path: 转换后的输出位置
    Returns:

    """
    if input_file is not None and output_path is not None:  # 兼容1.0.1版本
        mainPDF.pdf2docx(input_file=input_file, output_file=output_path)
    elif input_file is not None and output_file is not None:  # 优先单个识别
        mainPDF.pdf2docx(input_file=input_file, output_file=output_file)
    elif input_path is not None and output_path is not None:
        batch_main_pdf.pdf2docx(input_path=input_path, output_path=output_path)
    else:
        logger.error(
            "参数填写错误，详见：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/")


def pdf2imgs(input_file=None, output_file=None, input_path=None, output_path=None, merge=False):
    """
    pdf批量转图片 视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/
    > version 1.0.1
    Args:
        input_file: 输入的单个pdf的存储位置。
        output_file: 输出的单个word的存储位置，需要带后缀.docx
        input_path: 批量转换的pdf输入位置
        output_path: 批量转换后word的输出位置
    Returns:
    <= version 1.0.1
    Args:
        input_file: pdf的存储位置。
        output_path: 转换后的输出位置
    Returns:
    """
    if input_file is not None and output_path is not None:  # <= version 1.0.1
        mainPDF.pdf2imgs(input_file=input_file, output_file=output_file, merge=merge)
    elif input_file is not None and output_file is not None:
        mainPDF.pdf2imgs(input_file=input_file, output_file=output_file, merge=merge)
    elif input_path is not None and output_path is not None:
        batch_main_pdf.pdf2imgs(input_path=input_path, output_path=output_path, merge=merge)
    else:
        logger.error(
            "参数填写错误，详见：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/")


@cli.command()
@click.option('--input_file', default=None)
@click.option('--output_file', default=None)
@click.option('--input_path', default=None)
@click.option('--output_path', default=None)
def txt2pdf(input_file: str = None, output_file=None, input_path=None, output_path=None):
    """
    将文本文件转换为PDF文件。 视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/

    Args:
        input_file (str): 输入的文本文件路径。
        output_file (str, optional): 输出的PDF文件路径。默认为'txt2pdf.pdf'。

    Returns:
        None
    """

    if input_file is not None and output_file is not None:
        mainPDF.txt2pdf(input_file, output_file)
    elif input_path is not None and output_path is not None:
        batch_main_pdf.txt2pdf(input_path=input_path, output_path=output_path)
    else:
        logger.error(
            "参数填写错误，详见：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/")


def split4pdf(input_file=None, output_file=None, input_path=None, output_path=None, from_page=1, to_page=-1):
    """
    截取目标页范围的 PDF视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/

    Args:
        input_file: 输入的单个pdf的存储位置。
        output_file: 输出的单个pdf的存储位置，需要带后缀.pdf
        input_path: 批量切割的pdf输入位置
        output_path: 批量切割后pdf的输出位置
    Returns:
    """
    if input_file is not None and output_file is not None:
        mainPDF.split4pdf(input_file=input_file, output_file=output_file, from_page=from_page, to_page=to_page)

        return True
    elif input_path is not None and output_path is not None:
        batch_main_pdf.split4pdfs(input_path=input_path, output_path=output_path, from_page=from_page, to_page=to_page)

        return True
    else:
        logger.error("参数填写错误")
        return False


def encrypt4pdf(password, output_file, input_file=None, input_path=None):
    """
    加密pdf 视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/5-encrypt4pdf/
    演示代码：
    """
    mainPDF.encrypt4pdf(input_file=input_file, password=password, output_file=output_file, input_path=input_path)


@cli.command()
@click.option('--input_file', default=None)
@click.option('--output_file', default=None)
@click.option('--input_path', default=None)
@click.option('--output_path', default=None)
@click.option('--password', required=True, default=None)
def decrypt4pdf(input_file=None, password=None, output_file='decrypt.pdf', input_path=None, output_path=None):
    """
    解密pdf 视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/6-decrypt4pdf/
    > version 1.0.1 ？
    Args:
        input_file: 输入的单个pdf的存储位置。
        output_file: 输出的单个pdf的存储位置，需要带后缀.pdf
        input_path: 批量转换的pdf输入位置
        output_path: 批量转换后pdf的输出位置
        password : pdf解密密码

    Returns:
    <= version 1.0.1
    Args:
        input_file: pdf的存储位置。
        output_file: 转换后的输出位置
        password : pdf解密密码
    Returns:

    """
    if input_file is not None and output_file is not None:  # 兼容1.0.1版本
        mainPDF.decrypt4pdf(input_file=input_file, password=password, output_file=output_file)
    elif input_path is not None and output_path is not None:
        batch_main_pdf.pdf2decryptBatch(input_path=input_path, output_path=output_path, password=password)
    else:
        logger.error("参数填写错误，详见：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA")


def add_text_watermark(input_file, point, text='python-office',
                       output_file='./pdf_watermark.pdf', fontname="Helvetica", fontsize=12, color=(1, 0, 0)) -> None:
    """
    在PDF文档中添加文本水印。视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/7-add_text_watermark/

    Args:
        input_file (str): 要添加水印的PDF文件路径。
        point (tuple): 水印文本的位置，格式为(x, y)。
        text (str, optional): 要添加的水印文本。默认为'python-office'。
        output_file (str, optional): 输出文件的路径。默认为'./pdf_watermark.pdf'。
        fontname (str, optional): 字体名称。默认为'Helvetica'。
        fontsize (int, optional): 字体大小。默认为12。
        color (tuple, optional): 字体颜色，格式为(R, G, B)。默认为(1, 0, 0)，即红色。

    Returns:
        None
    """
    mainPDF.add_watermark(input_file, point, text,
                          output_file, fontname, fontsize, color)


def merge2pdf(input_file_list, output_file):
    """
    合并pdf 视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf/
    演示代码：
    """
    mainPDF.merge2pdf(input_file_list, output_file)


def del4pdf(page_nums, input_file=None, output_file=None, input_path=None, output_path=None):
    """
     删除pdf中的指定页码 视频&文档：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf/
    """
    if input_file is not None and output_file is not None and page_nums is not None:
        mainPDF.del4pdf(page_nums=page_nums, input_file=input_file, output_file=output_file)
    elif input_path is not None and output_path is not None and page_nums is not None:
        batch_main_pdf.del4pdf(page_nums=page_nums, input_path=input_path, output_path=output_path)
    else:
        logger.error(
            "参数填写错误，详见：http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf/")


########################################### 下面是不推荐使用的 ###########################################


# 给pdf加水印-无参数
def add_watermark():
    logger.warning("该功能已更新为：add_text_watermark")


def add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out):
    """
    文档：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA
    演示代码：
    """
    mainPDF.add_img_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)


# 给pdf加水印-有参数
def add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name) -> None:
    """
    必填参数：
    pdf_file:pdf的位置，例如：d:/code/程序员晚枫.pdf
    mark_str:需要添加的水印内容，例如：百度一下：程序员晚枫
    选填参数：
    output_file_name：指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.pdf
    """
    mainPDF.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)


# 修改pdf文件的作者和时间-有参数

def add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name) -> None:
    """
    必填参数：
    pdf_file:pdf的位置，例如：d:/code/程序员晚枫.pdf
    mark_str:需要添加的水印内容，例如：百度一下：程序员晚枫
    选填参数：
    output_file_name：指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.pdf
    """
    mainPDF.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)
