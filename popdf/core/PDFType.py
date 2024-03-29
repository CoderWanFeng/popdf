# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/Nt8E8vC-ZsoN1McTOYbY2g
@个人网站 ：www.python-office.com
@Date    ：2023/4/3 23:05
@Description     ：
'''
import os
from pathlib import Path

import fitz  # fitz就是pip install PyMuPDF
import pikepdf
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter  # PdfFileReader, PdfFileWriter,
from fpdf import FPDF
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

    def txt2pdf(self, path, res_pdf='file2pdf.pdf', output_path=r'./'):
        abs_path = Path(path).absolute()
        suffix = '.txt'
        txt_list = get_files(path=str(abs_path), suffix=suffix)
        exsit, abs_output_path = mkdir(output_path)
        for index, txt in simple_progress(enumerate(txt_list)):
            pdf = FPDF()
            pdf.add_page()  # Add a page
            pdf.set_font("Arial", size=15)  # set style and size of font
            file_content = open(txt, "r", encoding='utf8')  # open the text file in read mode
            # insert the texts in pdf
            for content in file_content:
                pdf.cell(50, 5, txt=content, ln=1, align='C')
            if index == 0:
                pdf.output(os.path.join(abs_output_path, res_pdf))
            else:
                pdf.output(os.path.join(abs_output_path, f'{str(index)} - {res_pdf}'))

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
    def encrypt4pdf(self, path, password, output_path, suffix='.pdf'):
        """
        @Author & Date  : CoderWanFeng 2022/5/9 18:27
        @Desc  : path: 存放文件的路径
                password: 你的密码
                res_pdf: 结果文件的名称 ，可以为空，默认是：encrypt.pdf
        """
        abs_path = Path(path).absolute()
        pdf_list = get_files(path=str(abs_path), suffix=suffix)
        for index, pdf_file in simple_progress(enumerate(pdf_list)):
            pdf = pikepdf.open(pdf_file)
            output_path = r'./' if output_path == None else output_path
            pdf.save(str(Path(output_path).absolute()) + '//' + Path(pdf_file).stem + '（加密）' + suffix,
                     encryption=pikepdf.Encryption(owner=password, user=password, R=4))
            pdf.close()
        # print("encrypt4pdf，该功能已过期")

    # PDF解密
    def decrypt4pdf(self, path, password, res_pdf='decrypt.pdf'):
        pdf = pikepdf.open(path, password=password)
        pdf.save(res_pdf)
        pdf.close()

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
