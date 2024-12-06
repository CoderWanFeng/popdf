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

import fitz  # fitz就是pip install PyMuPDF
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter  # PdfFileReader, PdfFileWriter,
from pdf2docx import Converter
from pofile import get_files, mkdir
from poprogress import simple_progress

from popdf.lib.pdf import add_watermark_service


class MainPDF():

    def add_watermark(self):
        pdf_file_in = input("请输入需要添加水印的文件位置：")  # 需要添加水印的文件
        Watermark_Str = input("请输入需要添加的水印内容：")
        print('=' * 20)
        print('正在按要求，给你的PDF文件添加水印，请让程序飞一会儿~')
        print('=' * 20)
        pdf_file_mark = 'watermark.pdf'  # 水印文件
        add_watermark_service.create_watermark(str(Watermark_Str))
        pdf_file_out = '添加了水印的文件.pdf'  # 添加PDF水印后的文件
        add_watermark_service.pdf_add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
        print("水印添加结束，请打开电脑上的这个位置，查看结果文件：{path}".format(path=os.getcwd()))

    def add_watermark_by_parameters(self, pdf_file, mark_str, output_path, output_file_name):
        """
        给pdf添加水印，需要参数的版本
        """
        # pdf_file_in = input("请输入需要添加水印的文件位置：")  # 需要添加水印的文件
        # Watermark_Str = input("请输入需要添加的水印内容：")
        print('=' * 20)
        print('正在按要求，给你的PDF文件添加水印，请让程序飞一会儿~')
        print('=' * 20)
        _input_pdf_file = Path(pdf_file).absolute()
        if not output_file_name:
            output_file_name = '（加了水印的）' + _input_pdf_file.name
        if output_path:
            _out_pdf_file = Path(output_path).absolute() / output_file_name  # '添加了水印的文件.pdf'
        else:
            _out_pdf_file = Path(_input_pdf_file.parent).absolute() / output_file_name  # '添加了水印的文件.pdf'

        _temp_pdf = _input_pdf_file.parent / '32012356985422-watermark.pdf'  # 水印文件
        add_watermark_service.create_watermark(_temp_pdf, str(mark_str))  # 水印文件
        add_watermark_service.pdf_add_watermark(_input_pdf_file, _temp_pdf, _out_pdf_file)
        print(f"水印添加结束，请打开电脑上的这个位置，查看结果文件：{_out_pdf_file}")

    def txt2pdf(self, input_path, output_path='file2pdf.pdf'):

        # https://fitz.readthedocs.io/en/latest/recipes-common-issues-and-their-solutions.html#how-to-convert-any-document-to-pdf
        if not (list(map(int, fitz.VersionBind.split("."))) >= [1, 14, 0]):
            raise SystemExit("need PyMuPDF v1.14.0+")

        print("Converting '%s' to '%s.pdf'" % (input_path, output_path))

        doc = fitz.open(input_path)

        b = doc.convert_to_pdf()  # convert to pdf
        pdf = fitz.open("pdf", b)  # open as pdf

        toc = doc.get_toc()  # table of contents of input
        pdf.set_toc(toc)  # simply set it for output
        meta = doc.metadata  # read and set metadata
        if not meta["producer"]:
            meta["producer"] = "PyMuPDF v" + fitz.VersionBind

        if not meta["creator"]:
            meta["creator"] = "PyMuPDF PDF converter"
        meta["modDate"] = fitz.get_pdf_now()
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
                if l["kind"] == fitz.LINK_NAMED:  # we do not handle named links
                    print("named link page", pinput.number, l)
                    link_skip += 1  # count them
                    continue
                pout.insert_link(l)  # simply output the others

        # save the conversion result
        pdf.save(output_path, garbage=4, deflate=True)
        # say how many named links we skipped
        if link_cnti > 0:
            print("Skipped %i named links of a total of %i in input." % (link_skip, link_cnti))

    def pdf2docx(self, file_path, output_path, pdfSuffix='.pdf', docxSuffix=".docx"):
        waiting_covert_pdf_files = get_files(file_path, suffix=pdfSuffix)
        if waiting_covert_pdf_files:
            for pdf_file in waiting_covert_pdf_files:
                word_name = os.path.basename(pdf_file)[:-4] + docxSuffix
                mkdir(Path(output_path))
                word_path = Path(output_path) / word_name
                cv = Converter(pdf_file)
                cv.convert(word_path)
                cv.close()

    # 合并pdf
    def merge2pdf(self, one_by_one, output):
        """
        @Author & Date  : CoderWanFeng 2022/5/16 23:33
        @Desc  : merge_pdfs(paths=['开篇词.pdf', '中国元宇宙白皮书 (送审稿).pdf'], output='merge.pdf')
        """
        pdf_writer = PdfWriter()

        for path in one_by_one:
            pdf_reader = PdfReader(path)
            # for page in tqdm(range(pdf_reader.getNumPages())):
            for page in simple_progress(range(len(pdf_reader.pages))):
                # 把每张PDF页面加入到这个可读取对象中
                # pdf_writer.addPage(pdf_reader.getPage(page))
                pdf_writer.add_page(pdf_reader.pages[page])

        # 把这个已合并了的PDF文档存储起来
        with open(output, 'wb') as out:
            pdf_writer.write(out)

    # PDF加密
    def encrypt4pdf(self, input_path, password, output_path, suffix='.pdf'):
        """
        @Author & Date  : CoderWanFeng 2022/5/9 18:27
        @Desc  : path: 存放文件的路径
                password: 你的密码
                res_pdf: 结果文件的名称 ，可以为空，默认是：encrypt.pdf
        """
        # abs_path = Path(input_path).absolute()
        # pdf_list = get_files(path=str(abs_path), suffix=suffix)
        # for index, pdf_file in simple_progress(enumerate(pdf_list)):
        with open(input_path, 'rb') as file:
            reader = PdfReader(file)

            # 创建一个PdfFileWriter对象
            writer = PdfWriter()

            # 将每一页加入到writer中
            for page in range(len(reader.pages)):
                writer.add_page(reader.pages[page])

            # 加密PDF
            writer.encrypt(password)

            # 写入加密后的PDF
            with open(output_path, 'wb') as out:
                writer.write(out)

    # PDF解密
    def decrypt4pdf(self, input_path, password, output_path='decrypt.pdf'):
        # 创建一个PdfReader对象，并提供密码来解密PDF文件
        pdf_reader = PdfReader(input_path, password=password)

        # 创建一个PdfWriter对象
        pdf_writer = PdfWriter()

        # 逐页将解密后的PDF添加到新的PDF文件中
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # 将解密后的PDF写入文件
        with open(output_path, 'wb') as out:
            pdf_writer.write(out)

    # print("decrypt4pdf，该功能已过期")

    # def pdf2imgs(self, pdf_path: str, out_dir=".") -> None:
    #     print('PDF开始转换，你可以加入交流群唠唠嗑：http://www.python4office.cn/wechat-group/')
    #     pdfDoc = fitz.open(pdf_path)
    #     if pdfDoc.pageCount > 50:
    #         print('少年，你的PDF页数有点多哟，请耐心等待~')
    #     for pg in range(pdfDoc.pageCount):
    #         page = pdfDoc[pg]
    #         rotate = int(0)
    #         # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
    #         # 此处若是不做设置，默认图片大小为：792X612, dpi=96
    #         zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
    #         zoom_y = 1.33333333
    #         mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    #         pix = page.getPixmap(matrix=mat, alpha=False)

    #         if not os.path.exists(out_dir):  # 判断存放图片的文件夹是否存在
    #             os.makedirs(out_dir)  # 若图片文件夹不存在就创建

    #         pix.writePNG(out_dir + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内
    #     print(f'PDF转换Image完成，图片在你指定的output文件夹{out_dir}，如果没有指定，默认是PDF同一个文件夹')

    def pdf2imgs(self, pdf_path: str, out_dir="./", merge: bool = False) -> None:
        pdf_file_list = get_files(pdf_path, suffix='.pdf')
        print('PDF开始转换，你可以加入交流群唠唠嗑：http://www.python4office.cn/wechat-group/')
        for pdf_file in simple_progress(pdf_file_list):
            pdfDoc = fitz.open(pdf_file)
            if pdfDoc.page_count > 50:
                print('少年，你的PDF页数有点多哟，请耐心等待~')
            for pg in simple_progress(range(pdfDoc.page_count)):
                page = pdfDoc[pg]
                rotate = int(0)
                # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
                # 此处若是不做设置，默认图片大小为：792X612, dpi=96
                zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
                zoom_y = 1.33333333
                mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                abs_output = str(Path(out_dir).absolute())
                if not os.path.exists(abs_output):  # 判断存放图片的文件夹是否存在
                    os.makedirs(abs_output)  # 若图片文件夹不存在就创建
                pdf_file_name = Path(pdf_file).stem
                pix.save(abs_output + f'/ [{pdf_file_name}]-{pg}.jpg')  # 将图片写入指定的文件夹内

        print(f'PDF转换Image完成，图片在你指定的output文件夹{abs_output}，如果没有指定，默认是PDF同一个文件夹')
        if merge:
            """
            TODO：目前的问题：多个PDF批量转换后的图片，会合成在一张图里
            """
            self.generate_long_image(input_path=abs_output,
                                     output_path=os.path.join(abs_output, "merge_output"),
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

    def add_img_watermark(self, pdf_file_in, pdf_file_mark, pdf_file_out):
        add_watermark_service.pdf_add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)

    # def table2excel(self,):

    def split4pdf(self, input_path, output_path=None, from_page=None, to_page=None):
        """
        分割pdf文件。

        :param input_path: str, 必填, 输入PDF文件的路径。
        :param output_path: str, 选填,  输出分割后PDF文件的路径，默认为'./output_path/split_pdf.pdf'。
        :param from_page: int, 必填, 起始页码。
        :param to_page: int, 选填, 结束页码，默认为None，不填代表只要一页起始页码。
        :return: None
        """
        # 打开输入原始PDF文件
        pdf_document = fitz.open(input_path)

        # 如果没有指定输出路径，则使用默认值
        if output_path is None:
            output_path = r'./output_path/split_pdf.pdf'
        mkdir(Path(output_path).parent)

        # 创建一个新的PDF文档
        pdf_document_new = fitz.open()

        # 插入指定页码的PDF页面
        if from_page is not None and to_page is not None:
            pdf_document_new.insert_pdf(pdf_document, from_page, to_page)
        elif from_page is not None and to_page is None:
            pdf_document_new.insert_pdf(pdf_document, from_page, from_page)
        else:
            # 如果没有指定页码，则插入整个PDF文档
            pdf_document_new.insert_pdf(pdf_document)

        # 保存分割后的PDF文件
        pdf_document_new.save(output_path)

        # 关闭文件
        pdf_document.close()
        pdf_document_new.close()
