# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：http://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/4/3 23:05
@Description     ：
'''
from pathlib import Path

import pymupdf  # fitz就是pip install PyMuPDF
from PyPDF2 import PdfReader, PdfWriter  # PdfFileReader, PdfFileWriter,
from loguru import logger
from pofile import get_files, mkdir
from poprogress import simple_progress

from popdf.lib.del4pdf_utils import del_page
from popdf.lib.pdf import add_watermark_service
from popdf.lib.pdf2docx_utils import third_convert
from popdf.lib.split4pdf_utils import split_for_pdf
from popdf.lib.pdf2imgs_utils import pdf_to_merge_image, pdf_to_images

import os

class MainPDF():
    def __init__(self):
        self.pdf_suffix = '.pdf'

    def pdf2docx(self, input_file, output_file):
        if input_file:
            mkdir(Path(output_file).parent)
            third_convert(input_file, output_file)

    def pdf2imgs(self, input_file: str = None, output_file: str = None, merge: bool = False) -> None:
        if merge:
            mkdir(Path(output_file).parent)
            pdf_to_merge_image(input_file=input_file, output_file=output_file)
        else:
            mkdir(Path(output_file).absolute())
            pdf_to_images(input_file=input_file, output_path=output_file)

    def txt2pdf(self, input_file, output_file='file2pdf.pdf'):

        # https://pymupdf.readthedocs.io/en/latest/recipes-common-issues-and-their-solutions.html#how-to-convert-any-document-to-pdf
        if not (list(map(int, pymupdf.VersionBind.split("."))) >= [1, 14, 0]):
            raise SystemExit("need PyMuPDF v1.14.0+")

        print("Converting '%s' to '%s.pdf'" % (input_file, output_file))

        doc = pymupdf.open(input_file)

        b = doc.convert_to_pdf()  # convert to pdf
        pdf = pymupdf.open("pdf", b)  # open as pdf

        toc = doc.get_toc()  # table of contents of input
        pdf.set_toc(toc)  # simply set it for output
        meta = doc.metadata  # read and set metadata
        if not meta["producer"]:
            meta["producer"] = "PyMuPDF v" + pymupdf.VersionBind

        if not meta["creator"]:
            meta["creator"] = "PyMuPDF PDF converter"
        meta["modDate"] = pymupdf.get_pdf_now()
        meta["creationDate"] = meta["modDate"]
        pdf.set_metadata(meta)

        # now process the links
        link_cnti = 0
        link_skip = 0
        for pinput in doc:  # iterate through input pages
            links = pinput.get_links()  # get list of links
            link_cnti += len(links)  # count how many
            pout = pdf[pinput.number]  # read corresp. output page
            for l in links:  # iterate though the links
                if l["kind"] == pymupdf.LINK_NAMED:  # we do not handle named links
                    print("named link page", pinput.number, l)
                    link_skip += 1  # count them
                    continue
                pout.insert_link(l)  # simply output the others
        mkdir(Path(output_file).parent)
        # save the conversion result
        pdf.save(output_file, garbage=4, deflate=True)
        # say how many named links we skipped
        if link_cnti > 0:
            print("Skipped %i named links of a total of %i in input." % (link_skip, link_cnti))

    def split4pdf(self, input_file, output_file, from_page, to_page):
        """
        截取pdf文件。

        :param input_file: str, 必填, 输入PDF文件的路径。
        :param from_page: int, 必填, 起始页码。
        :param to_page: int, 选填, 结束页码，默认为None，不填代表只要一页起始页码。
        :param output_file: str, 选填,  输出分割后PDF文件的路径'。
        :return: None
        """
        if input_file:
            mkdir(Path(output_file).parent)
            split_for_pdf(input_file=input_file, output_file=output_file, from_page=from_page, to_page=to_page)




    # PDF加密
    def encrypt4pdf(self, input_file, password, output_file, suffix='.pdf', input_path=None):
        """
        @Author & Date  : CoderWanFeng 2022/5/9 18:27
        @Desc  : path: 存放文件的路径
                password: 你的密码
                res_pdf: 结果文件的名称 ，可以为空，默认是：encrypt.pdf
        """
        if input_path:
            pdf_files = get_files(path=input_path, suffix='.pdf')
        else:
            pdf_files = [str(Path(input_file).absolute())]
        if Path(output_file).absolute().parent == Path(pdf_files[0]).absolute().parent:
            logger.error('the output path is same to input path')
        else:
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
                    output_file_parent = Path(output_file).parent
                    mkdir(output_file_parent)
                    # 写入加密后的PDF
                    out_pdf = output_file_parent / Path(pdf_f).name

                    with open(out_pdf, 'wb') as out:
                        writer.write(out)
            logger.info("encrypt4pdf is success")

    # PDF解密
    def decrypt4pdf(self, input_file, password, output_file='decrypt.pdf'):
        # 创建一个PdfReader对象，并提供密码来解密PDF文件
        pdf_reader = PdfReader(input_file, password=password)

        # 创建一个PdfWriter对象
        pdf_writer = PdfWriter()

        # 逐页将解密后的PDF添加到新的PDF文件中
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
        mkdir(Path(output_file).parent)
        # 将解密后的PDF写入文件
        with open(output_file, 'wb') as out:
            pdf_writer.write(out)

    def add_img_watermark(self, pdf_file_in, pdf_file_mark, pdf_file_out):
        add_watermark_service.pdf_add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)

    # 合并pdf
    def merge2pdf(self, input_file_list, output_file):
        """
        @Author & Date  : CoderWanFeng 2022/5/16 23:33
        @Desc  : merge_pdfs(paths=['开篇词.pdf', '中国元宇宙白皮书 (送审稿).pdf'], output='程序员晚枫.pdf')
        """
        pdf_writer = PdfWriter()

        for pdf_file in input_file_list:
            pdf_reader = PdfReader(pdf_file)
            # for page in tqdm(range(pdf_reader.getNumPages())):
            for page in simple_progress(range(len(pdf_reader.pages))):
                # 把每张PDF页面加入到这个可读取对象中
                # pdf_writer.addPage(pdf_reader.getPage(page))
                pdf_writer.add_page(pdf_reader.pages[page])

        # 把这个已合并了的PDF文档存储起来
        with open(output_file, 'wb') as out:
            pdf_writer.write(out)

    # 删除指定页面
    def del4pdf(self, page_nums: list[int], input_file: str = None, output_file: str = None):
        """
        使用 pymupdf 从 PDF 文件中删除指定的页面。

        参数:
        page_nums (list): 需要删除的页面编号列表（基于0索引，注意页面编号不连续）。
        input_file (str): 输入的 PDF 文件路径。
        output_file (str): 输出（修改后）的 PDF 文件路径。
        """
        mkdir(Path(output_file).parent)
        del_page(page_nums, input_file, output_file)

    def add_watermark(self, input_file, point, text='程序员晚枫',
                      output_file='./pdf_watermark.pdf', fontname="Helvetica", fontsize=12, color=(1, 0, 0)):
        # 打开输入PDF文件
        doc = pymupdf.open(input_file)

        # 遍历PDF的每一页
        for page in doc:
            # 插入文本
            page.insert_text(point=point, text=text, fontname=fontname, fontsize=fontsize, color=color)
        mkdir(Path(output_file).parent)
        # 保存修改后的PDF文件
        doc.save(output_file)
        doc.close()  # 关闭PDF文件

    def file2pdf(self, input_file, output_file='file2pdf.pdf'):
        self.txt2pdf(input_file, output_file)

    # def table2excel(self,):
