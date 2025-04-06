# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：http://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/4/3 23:05
@Description     ：
'''
import os
from pathlib import Path

import pymupdf  # fitz就是pip install PyMuPDF
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter  # PdfFileReader, PdfFileWriter,
from loguru import logger
from pofile import get_files, mkdir
from poprogress import simple_progress

from popdf.lib.pdf import add_watermark_service
from popdf.lib.pdf2docx_utils import third_convert


class MainPDF():
    def __init__(self):
        self.pdf_suffix = '.pdf'

    def pdf2docx(self, input_file, output_file):
        if input_file:
            mkdir(Path(output_file).parent)
            third_convert(input_file, output_file)

    def pdf2imgs(self, input_file: str = None, output_file=None, merge: bool = False) -> None:
        pdfDoc = pymupdf.open(input_file)
        page_count = pdfDoc.page_count
        for pg in simple_progress(range(pdfDoc.page_count)):
            print(f'processing page： {pg}/{page_count}')
            page = pdfDoc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
            # 此处若是不做设置，默认图片大小为：792X612, dpi=96
            zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
            zoom_y = 1.33333333
            mat = pymupdf.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            mkdir(output_path)
            pdf_file_name = Path(pdf_file).stem
            pix.save(output_path + f'/ {pdf_file_name}-{pg}.jpg')  # 将图片写入指定的文件夹内

        print(f'PDF转换Image完成，图片在你指定的output文件夹{output_path}，如果没有指定，默认是PDF同一个文件夹')
        if merge:
            """
            TODO：目前的问题：多个PDF批量转换后的图片，会合成在一张图里
            """
            self.generate_long_image(input_path=output_path,
                                     output_path=os.path.join(output_path, "merge_output"),
                                     img_name=pdf_file_name + '.jpg')

    def generate_long_image(self, input_path: str, output_path, img_name='merge.jpg'):
        """
        将ppt的各个页面拼接成长图：https://blog.csdn.net/m0_51777056/article/details/130262561
        :param input_path:
        :param output_path:
        :param img_name:
        :return:
        """
        # 获取图片列表
        img_list = []
        for imgs in os.listdir(input_path):
            img_list.append(os.path.join(input_path, imgs))

        # 将获取到ppt的页面进行排序
        ims_sort = sorted(img_list, key=lambda jpg: len(jpg))

        width, height = Image.open(img_list[0]).size  # 取第一个图片尺寸
        img_mode = Image.open(img_list[0]).mode
        long_canvas = Image.new(img_mode, (width, height * len(img_list)))  # 创建同宽，n倍高的空白图片

        # 拼接图片
        for i, image in enumerate(ims_sort):
            long_canvas.paste(Image.open(image), box=(0, i * height))
        mkdir(output_path)
        long_canvas.save(os.path.join(output_path, img_name))  # 保存长图

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


# def table2excel(self,):

def split4pdf(self, input_file, output_file=r'./output_path/split_pdf.pdf', from_page=-1, to_page=-1):
    """
    分割pdf文件。

    :param input_path: str, 必填, 输入PDF文件的路径。
    :param output_path: str, 选填,  输出分割后PDF文件的路径，默认为'./output_path/split_pdf.pdf'。
    :param from_page: int, 必填, 起始页码。
    :param to_page: int, 选填, 结束页码，默认为None，不填代表只要一页起始页码。
    :return: None
    """
    # 打开输入原始PDF文件
    pdf_document = pymupdf.open(input_file)

    # 如果没有指定输出路径，则使用默认值
    mkdir(Path(output_file).parent)

    # 创建一个新的PDF文档
    pdf_document_new = pymupdf.open()

    pdf_document_new.insert_pdf(pdf_document, from_page, to_page)

    # 保存分割后的PDF文件
    pdf_document_new.save(output_file)

    # 关闭文件
    pdf_document.close()
    pdf_document_new.close()


# 删除指定页面
def del4pdf(self, input_file, page_nums, output_file):
    """
    使用 pymupdf 从 PDF 文件中删除指定的页面。

    参数:
    input_file (str): 输入的 PDF 文件路径。
    page_nums (list): 需要删除的页面编号列表（基于0索引，注意页面编号不连续）。
    output_file (str): 输出（修改后）的 PDF 文件路径。
    """
    # 打开输入的 PDF 文件
    doc = pymupdf.open(input_file)

    # 创建一个新的 PDF writer 对象（实际上在 pymupdf 中我们不需要显式的 writer 对象，
    # 但我们可以创建一个新的文档来模拟这个过程）
    new_doc = pymupdf.open()

    # 遍历所有页面
    for page_num in range(len(doc)):
        # 如果当前页面编号不在删除列表中，则添加到新的文档中
        if page_num not in page_nums:
            new_page = new_doc.new_page(width=doc.page_rect(page_num).width, height=doc.page_rect(page_num).height)
            new_page.show_pdf_page(doc, page_num)  # 将原文档的页面内容复制到新页面

    # 关闭原始文档（不需要保存）
    doc.close()

    # 将新文档保存到输出文件
    new_doc.save(output_file)
    new_doc.close()
