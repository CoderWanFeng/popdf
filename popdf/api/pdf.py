# -*- coding: utf-8 -*-
from loguru import logger

from popdf.core.PDFType import MainPDF

mainPDF = MainPDF()


# 给pdf加水印-无参数
# @except_dec()
def add_watermark():
    logger.warning("该功能已更新为：add_text_watermark")


def add_text_watermark(input_file, point, text='python-office',
                       output_file='./pdf_watermark.pdf', fontname="Helvetica", fontsize=12, color=(1, 0, 0)) -> None:
    """
    在PDF文档中添加文本水印。

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


def txt2pdf(input_file: str, output_file='txt2pdf.pdf'):
    """
    将文本文件转换为PDF文件。

    Args:
        input_file (str): 输入的文本文件路径。
        output_file (str, optional): 输出的PDF文件路径。默认为'txt2pdf.pdf'。

    Returns:
        None
    """

    mainPDF.txt2pdf(input_file, output_file)


# PDF加密
# @except_dec()
def encrypt4pdf( password, output_file,input_file=None,input_path=None):
    """
    加密pdf
    文档：https://blog.csdn.net/weixin_42321517/article/details/129963432
    演示代码：
    """
    mainPDF.encrypt4pdf(input_file=input_file, password=password, output_file=output_file,input_path=input_path)


# PDF解密
# @except_dec()
def decrypt4pdf(input_file, password, output_file='decrypt.pdf'):
    """
    解密pdf
    文档：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA
    演示代码：
    """
    mainPDF.decrypt4pdf(input_file, password, output_file)


# 合并pdf
# @except_dec()
def merge2pdf(input_file_list, output_file):
    """
    合并pdf
    文档：https://baijiahao.baidu.com/s?id=1733062611567959337
    演示代码：
    """
    mainPDF.merge2pdf(input_file_list, output_file)


# todo：输入文件路径
# @except_dec()
def pdf2docx(input_file, output_path='.'):
    """
    PDF转Word
    视频：https://www.bilibili.com/video/BV1em4y1H7ir/
    Args:
        input_file: pdf的存储位置。批量处理：只填写文件夹就行
        output_path: 转换后的输出位置

    Returns:

    """
    mainPDF.pdf2docx(input_file, output_path)


# @except_dec()
def pdf2imgs(input_file, output_path, merge=False):
    """
    pdf转图片
    文档：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA
    演示代码：
    """
    mainPDF.pdf2imgs(input_file, output_path, merge)



# @except_dec()
def pdf2imgsinbulk(input_path, output_path, merge=False):
    """
    pdf批量转图片 
    文档：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA
    演示代码：
    Args:
        input_path: pdf的存储位置。批量处理：只填写文件夹就行
        output_path: 转换后的输出位置
    """
    import os	
    def traverse_dir(path):
        files = []
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                traverse_dir(file_path)
            else:
                files.append(file_path)
        return files
    
    
    files = traverse_dir(input_path)
    files_pdf = [f for f in files if os.path.splitext(f)[1] in [".pdf"]]
    
    for input_file in files_pdf:
        base_filename = os.path.basename(input_file)
        file_name = os.path.splitext(base_filename)[0]
        dest_path = os.path.join(output_path, file_name)
        mainPDF.pdf2imgs(input_file, dest_path, merge)
		

def split4pdf(input_file, output_file=r'./output_path/split_pdf.pdf', from_page=-1, to_page=-1):
    mainPDF.split4pdf(input_file, output_file, from_page, to_page)


def del4pdf(input_file, page_nums, output_file):
    mainPDF.del4pdf(input_file, page_nums, output_file)


########################################### 下面是不推荐使用的 ###########################################

# @except_dec()
def add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out):
    """
    文档：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA
    演示代码：
    """
    mainPDF.add_img_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)


# 给pdf加水印-有参数
# @except_dec()
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
# @except_dec()
def add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name) -> None:
    """
    必填参数：
    pdf_file:pdf的位置，例如：d:/code/程序员晚枫.pdf
    mark_str:需要添加的水印内容，例如：百度一下：程序员晚枫
    选填参数：
    output_file_name：指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.pdf
    """
    mainPDF.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)
