# -*- coding: utf-8 -*-
from popdf.core.PDFType import MainPDF

mainPDF = MainPDF()


# 给pdf加水印-无参数
# @except_dec()
def add_watermark() -> None:
    """
    加水印
    视频：https://www.bilibili.com/video/BV1Se411T7au
    演示代码：
    """
    mainPDF.add_watermark()


# txt转pdf
# @except_dec()
def txt2pdf(path: str, res_pdf='txt2pdf.pdf', output_path=r'./'):
    """
    txt转pdf
    文档：https://blog.csdn.net/weixin_42321517/article/details/130612189
    演示代码：
    """
    mainPDF.txt2pdf(path, res_pdf, output_path)


# PDF加密
# @except_dec()
def encrypt4pdf(path, password, output_path):
    """
    加密pdf
    文档：https://blog.csdn.net/weixin_42321517/article/details/129963432
    演示代码：
    """
    mainPDF.encrypt4pdf(path, password, output_path)


# PDF解密
# @except_dec()
def decrypt4pdf(path, password, res_pdf='decrypt.pdf'):
    """
    解密pdf
    文档：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA
    演示代码：
    """
    mainPDF.decrypt4pdf(path, password, res_pdf)


# 合并pdf
# @except_dec()
def merge2pdf(one_by_one, output):
    """
    合并pdf
    文档：https://baijiahao.baidu.com/s?id=1733062611567959337
    演示代码：
    """
    mainPDF.merge2pdf(one_by_one, output)


# todo：输入文件路径
# @except_dec()
def pdf2docx(file_path, output_path='.'):
    """
    PDF转Word
    视频：https://www.bilibili.com/video/BV1em4y1H7ir/
    Args:
        file_path: pdf的存储位置。批量处理：只填写文件夹就行
        output_path: 转换后的输出位置

    Returns:

    """
    mainPDF.pdf2docx(file_path, output_path)


# @except_dec()
def pdf2imgs(pdf_path, out_dir, merge=False):
    """
    pdf转图片
    文档：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA
    演示代码：
    """
    mainPDF.pdf2imgs(pdf_path, out_dir, merge)


# @except_dec()
def add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out):
    """
    文档：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA
    演示代码：
    """
    mainPDF.add_img_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)


########################################### 下面是不推荐使用的 ###########################################

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


def split4pdf(input_path, output_path=r'./output_path/split_pdf.pdf', from_page=None, to_page=None):
    mainPDF.split4pdf(input_path, output_path, from_page, to_page)
