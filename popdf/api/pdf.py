# -*- coding: utf-8 -*-
"""
popdf API模块 - PDF处理工具库的对外接口

提供以下功能：
- PDF转Word
- PDF转图片
- TXT转PDF
- PDF分割/合并
- PDF加密/解密
- 添加水印

示例用法：
>>> import popdf
>>> popdf.pdf2docx(input_file='input.pdf', output_file='output.docx')
"""
import click
from loguru import logger
from typing import Optional, Union, List, Tuple

from popdf.core.Batch_PDFType import Batch_PDFType
from popdf.core.PDFType import MainPDF

mainPDF = MainPDF()
batch_main_pdf = Batch_PDFType()


@click.group()
def cli():
    """popdf命令行工具入口"""
    logger.info("popdf 命令行工具，查看帮助：popdf --help")


def pdf2docx(
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None:
    """
    将PDF文件转换为Word文档（.docx格式）

    支持单文件转换和批量转换两种模式。

    Args:
        input_file: 输入的单个PDF文件路径，例如：'/path/to/file.pdf'
        output_file: 输出的单个Word文件路径，需要带.docx后缀，例如：'/path/to/output.docx'
        input_path: 批量转换时，输入PDF文件所在的目录路径
        output_path: 批量转换时，输出Word文件的目录路径

    Examples:
        # 单文件转换
        >>> popdf.pdf2docx(input_file='document.pdf', output_file='document.docx')

        # 批量转换
        >>> popdf.pdf2docx(input_path='/pdfs/', output_path='/docs/')

    Returns:
        None

    Raises:
        ValueError: 当参数填写错误时
    """
    if input_file is not None and output_file is not None:
        mainPDF.pdf2docx(input_file=input_file, output_file=output_file)
    elif input_path is not None and output_path is not None:
        batch_main_pdf.pdf2docx(input_path=input_path, output_path=output_path)
    elif input_file is not None and output_path is not None:
        mainPDF.pdf2docx(input_file=input_file, output_file=output_path)
    else:
        logger.error(
            "参数填写错误，详见：https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/")
        raise ValueError("请提供正确的参数组合：input_file+output_file 或 input_path+output_path")


def pdf2imgs(
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None,
    merge: bool = False
) -> None:
    """
    将PDF文件转换为图片

    Args:
        input_file: 输入的单个PDF文件路径
        output_file: 输出的图片文件路径（合并模式时使用）
        input_path: 批量转换时，输入PDF文件所在的目录路径
        output_path: 批量转换时，输出图片的目录路径
        merge: 是否将多页PDF合并为一张图片，默认为False

    Examples:
        # 转换为多张图片
        >>> popdf.pdf2imgs(input_file='document.pdf', output_path='/images/')

        # 合并为单张图片
        >>> popdf.pdf2imgs(input_file='document.pdf', output_file='merged.png', merge=True)
    """
    if input_file is not None and output_file is not None:
        mainPDF.pdf2imgs(input_file=input_file, output_file=output_file, merge=merge)
    elif input_path is not None and output_path is not None:
        batch_main_pdf.pdf2imgs(input_path=input_path, output_path=output_path, merge=merge)
    else:
        logger.error(
            "参数填写错误，详见：https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/")


def txt2pdf(
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None:
    """
    将文本文件转换为PDF文件

    Args:
        input_file: 输入的单个TXT文件路径
        output_file: 输出的PDF文件路径，默认为'txt2pdf.pdf'
        input_path: 批量转换时，输入TXT文件所在的目录路径
        output_path: 批量转换时，输出PDF文件的目录路径

    Examples:
        >>> popdf.txt2pdf(input_file='readme.txt', output_file='readme.pdf')
    """
    if input_file is not None and output_file is not None:
        mainPDF.txt2pdf(input_file, output_file)
    elif input_path is not None and output_path is not None:
        batch_main_pdf.txt2pdf(input_path=input_path, output_path=output_path)
    else:
        logger.error(
            "参数填写错误，详见：https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/")


def split4pdf(
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None,
    from_page: int = 1,
    to_page: int = -1
) -> bool:
    """
    截取PDF文件的指定页面范围

    Args:
        input_file: 输入的单个PDF文件路径
        output_file: 输出的PDF文件路径，需要带.pdf后缀
        input_path: 批量切割时，输入PDF文件所在的目录路径
        output_path: 批量切割时，输出PDF文件的目录路径
        from_page: 起始页码，默认为1
        to_page: 结束页码，默认为-1（表示最后一页）

    Returns:
        bool: 转换成功返回True，失败返回False

    Examples:
        >>> popdf.split4pdf(input_file='document.pdf', output_file='pages_1-5.pdf', from_page=1, to_page=5)
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


def encrypt4pdf(
    password: str,
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None:
    """
    给PDF文件添加密码保护（加密）

    Args:
        password: 加密密码
        input_file: 输入的单个PDF文件路径
        output_file: 输出的加密PDF文件路径
        input_path: 批量加密时，输入PDF文件所在的目录路径
        output_path: 批量加密时，输出加密PDF文件的目录路径

    Examples:
        >>> popdf.encrypt4pdf(password='mypassword', input_file='document.pdf', output_file='encrypted.pdf')
    """
    mainPDF.encrypt4pdf(password=password, input_file=input_file, output_file=output_file, 
                        input_path=input_path, output_path=output_path)


def decrypt4pdf(
    input_file: Optional[str] = None,
    password: Optional[str] = None,
    output_file: str = 'decrypt.pdf',
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None:
    """
    解密受密码保护的PDF文件

    Args:
        input_file: 输入的单个加密PDF文件路径
        password: PDF解密密码
        output_file: 输出的解密PDF文件路径，默认为'decrypt.pdf'
        input_path: 批量解密时，输入加密PDF文件所在的目录路径
        output_path: 批量解密时，输出解密PDF文件的目录路径

    Examples:
        >>> popdf.decrypt4pdf(input_file='encrypted.pdf', password='mypassword', output_file='decrypted.pdf')
    """
    if input_file is not None:
        mainPDF.decrypt4pdf(input_file=input_file, password=password, output_file=output_file)
    elif input_path is not None and output_path is not None:
        batch_main_pdf.pdf2decryptBatch(input_path=input_path, output_path=output_path, password=password)
    else:
        logger.error("参数填写错误，详见：https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA")


def add_text_watermark(
    input_file: str,
    point: Tuple[int, int],
    text: str = 'www.python-office.com',
    output_file: str = './pdf_watermark.pdf',
    fontname: str = "Helvetica",
    fontsize: int = 12,
    color: Tuple[float, float, float] = (1, 0, 0)
) -> None:
    """
    在PDF文档中添加文本水印

    Args:
        input_file: 要添加水印的PDF文件路径
        point: 水印文本的位置，格式为(x, y)，例如：(100, 100)
        text: 要添加的水印文本，默认为'www.python-office.com'
        output_file: 输出文件的路径，默认为'./pdf_watermark.pdf'
        fontname: 字体名称，默认为'Helvetica'
        fontsize: 字体大小，默认为12
        color: 字体颜色，格式为(R, G, B)，取值范围0-1，默认为红色(1, 0, 0)

    Examples:
        >>> popdf.add_text_watermark(input_file='document.pdf', point=(100, 100), text='机密', color=(0.5, 0.5, 0.5))
    """
    mainPDF.add_watermark(input_file, point, text, output_file, fontname, fontsize, color)


def merge2pdf(
    input_file_list: List[str],
    output_file: str
) -> None:
    """
    合并多个PDF文件为一个PDF文件

    Args:
        input_file_list: 要合并的PDF文件路径列表，例如：['file1.pdf', 'file2.pdf', 'file3.pdf']
        output_file: 合并后的PDF文件路径

    Examples:
        >>> popdf.merge2pdf(input_file_list=['part1.pdf', 'part2.pdf'], output_file='merged.pdf')
    """
    mainPDF.merge2pdf(input_file_list, output_file)


def del4pdf(
    page_nums: List[int],
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None:
    """
    删除PDF文件中的指定页码

    Args:
        page_nums: 要删除的页码列表，例如：[1, 3, 5]
        input_file: 输入的单个PDF文件路径
        output_file: 输出的PDF文件路径
        input_path: 批量删除时，输入PDF文件所在的目录路径
        output_path: 批量删除时，输出PDF文件的目录路径

    Examples:
        >>> popdf.del4pdf(page_nums=[2, 4], input_file='document.pdf', output_file='cleaned.pdf')
    """
    if input_file is not None and output_file is not None and page_nums is not None:
        mainPDF.del4pdf(page_nums=page_nums, input_file=input_file, output_file=output_file)
    elif input_path is not None and output_path is not None and page_nums is not None:
        batch_main_pdf.del4pdf(page_nums=page_nums, input_path=input_path, output_path=output_path)
    else:
        logger.error(
            "参数填写错误，详见：https://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf/")


# ============ 已废弃的函数 ============
def add_watermark():
    """已废弃，请使用 add_text_watermark"""
    logger.warning("该功能已更新为：add_text_watermark")


def add_img_water(pdf_file_in: str, pdf_file_mark: str, pdf_file_out: str):
    """
    已废弃 - 添加图片水印

    Args:
        pdf_file_in: 输入PDF文件路径
        pdf_file_mark: 水印图片PDF路径
        pdf_file_out: 输出PDF文件路径
    """
    logger.warning("该功能已更新，请查看文档了解新用法")
    mainPDF.add_img_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)


def add_watermark_by_parameters(pdf_file: str, mark_str: str, output_path: str, output_file_name: str = None) -> None:
    """已废弃，请使用 add_text_watermark"""
    logger.warning("该功能已更新为：add_text_watermark")
    mainPDF.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)