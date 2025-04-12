import os
import unittest

from popdf.api.pdf import *
from popdf.api.pdf import split4pdf
from loguru import logger




class TestPDF(unittest.TestCase):

    def test_pdf2docx(self):
        """
        version 1.0.1
        """
        base_dir = os.path.dirname(__file__)
        input_file = os.path.join(base_dir, '..', 'test_files', 'pdf2docx', '程序员晚枫.pdf')
        output_path = os.path.join(base_dir, '..', 'test_files', 'pdf2docx', 'docx', '1.docx')
        pdf2docx(
            input_file=input_file,
            output_path=output_path
        )

    def test_pdf2docx_single(self):
        """
        version 1.0.2
        """
        base_dir = os.path.dirname(__file__)
        input_file = os.path.join(base_dir, '..', 'test_files', 'pdf2docx', '程序员晚枫.pdf')
        output_file = os.path.join(base_dir, '..', 'test_files', 'pdf2docx', 'docx', '1.docx')
        pdf2docx(
            input_file=input_file,
            output_file=output_file
        )

    def test_pdf2docx_batch(self):
        """
        version 1.0.2
        """
        pdf2docx(
            input_path=r'../test_files/pdf2docx/',
            output_path=r'../test_files/pdf2docx/docx/'
        )

    def test_pdf2imgs(self):
        pdf2imgs(
            # ~ input_file=r'../test_files/pdf/程序员晚枫.pdf',
            input_file=r'../test_files/pdf2imgs/程序员晚枫.pdf',
            output_file='../test_files/pdf2imgs/imgs')

    def test_pdf2imgs_merge(self):
        pdf2imgs(
            input_file=r'../test_files/pdf2imgs/程序员晚枫.pdf',
            output_file='../test_files/pdf2imgs/imgs/1.jpg', merge=True)

    def test_batch_pdf2imgs(self):
        pdf2imgs(
            # ~ input_file=r'../test_files/pdf/程序员晚枫.pdf',
            input_path=r'../test_files/pdf2imgs',
            output_path='../test_files/pdf2imgs/imgs')

    def test_batch_pdf2imgs_merge(self):
        pdf2imgs(
            # ~ input_file=r'../test_files/pdf/程序员晚枫.pdf',
            input_path=r'../test_files/pdf2imgs',
            output_path='../test_files/pdf2imgs/imgs', merge=True)

    def test_txt2pdf(self):
        # 准备测试数据
        input_file = "../test_files/txt2pdf/程序员晚枫.txt"
        output_file = "../test_files/txt2pdf/程序员晚枫.pdf"
        # 调用被测方法
        txt2pdf(input_file=input_file, output_file=output_file)

    def test_batch_txt2pdf(self):
        # 准备测试数据
        input_path = "../test_files/txt2pdf/batch"
        output_path = "../test_files/txt2pdf/batch_res"
        # 调用被测方法
        txt2pdf(input_path=input_path, output_path=output_path)

    def test_split4pdf(self):
        split4pdf(
            input_file=r'../test_files/split4pdf/程序员晚枫.pdf',
            from_page=1,
            output_file=r'../test_files/split4pdf/split4pdf.pdf'
        )

    def test_encrypt4pdf(self):
        encrypt4pdf(
            input_file=r'../test_files/pdf/程序员晚枫.pdf',
            password='123456',
            output_file=r'./test_files/pdf/encrypt4pdf.pdf'
        )

    def test_decrypt4pdf(self):
        decrypt4pdf(
            input_file=r'./test_files/pdf/encrypt4pdf.pdf',
            password='123456',
            output_file=r'./test_files/pdf/decrypt4pdf.pdf'
        )

    # 兼容1.0.1版本
    def test_decrypt4pdf1(self):
        decrypt4pdf(
            input_file=r'./test_files/decrypt4pdf/out.pdf',
            password='123456',
            output_file=r'./test_files/decrypt4pdf/target/single.pdf'
        )

    # 批量解密
    def test_decrypt4pdf2(self):
        decrypt4pdf(
            input_path=r'./test_files/decrypt4pdf',
            password='123456',
            output_path=r'./test_files/decrypt4pdf/target'
        )

    # 参数异常
    def test_decrypt4pdf3(self):
        decrypt4pdf(
            input_path=None,
            password='123456',
            output_path=r'./test_files/decrypt4pdf/target'
        )
    # 参数异常
    def test_decrypt4pdf4(self):
        decrypt4pdf(
            input_path=None,
            password='123456',
            output_path=None
        )



    def test_add_text_watermark(self):
        add_text_watermark(input_file=r'../test_files/pdf/程序员晚枫.pdf', point=(50, 50),
                           output_file=r'./test_files/pdf/add_text_watermark.pdf')

    def test_merge2pdf(self):
        merge2pdf(
            input_file_list=[r'./test_files/pdf/程序员晚枫.pdf', r'./test_files/pdf/程序员晚枫.pdf'],
            output_file=r'./test_files/pdf/merge2pdf.pdf'
        )

    def test_del4pdf(self):
        del_pdf=r'../test_files/del4pdf/程序员晚枫.pdf'
        del4pdf(
            input_file=del_pdf,
            page_nums=[3],
            output_file=r'../test_files/del4pdf/a//del4pdf.pdf'
        )

    def test_del4pdf_batch(self):
        del_pdf=r'../test_files/del4pdf/'
        del4pdf(
            input_path=del_pdf,
            page_nums=[2],
            output_path=r'../test_files/del4pdf/b'
        )

    ##############  以下方法未测试  #################
    def test_add_img_water(self):
        add_img_water(pdf_file_in='./test_files/pdf/add_img.pdf', pdf_file_mark='../test_files/pdf/程序员晚枫.pdf',
                      pdf_file_out='add_img_res.pdf')

    def test_add_watermark_by_parameters(self):
        add_watermark_by_parameters(
            pdf_file=r'/tests/test_files/pdf/程序员晚枫.pdf',
            mark_str='python-office',
            output_path=None,
            output_file_name=None)

    def test_add_watermark(self):
        stub_stdin(self, './test_files/pdf/程序员晚枫.pdf\npython-office\n')  # 依次输入
        add_watermark()

    # def test_del4pdf(self):
    #     del4pdf(input_file="../test_files/del4pdf/程序员晚枫的粉丝福利.pdf",
    #             page_nums=[1, 3],
    #             output_file="tests/test_files/del4pdf/output_text/")

    def test_encrypt4pdf2(self):
        encrypt4pdf(
            password='123456',
            output_file="../test_files/encrypt4pdf/pc/out.pdf",
            input_path=r'../test_files/encrypt4pdf/pc'
        )


# 当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

class TestOCR(unittest.TestCase):
    """
    pdf.py测试用的代码
    """
    def test_split4pdf(self):
        input_file = os.path.abspath(os.path.join(base_dir, '..', '..', 'tests', 'test_files', 'pdf', '程序员晚枫.pdf'))
        output_file = os.path.abspath(os.path.join(base_dir, '..', '..', 'tests', 'test_files', 'pdf', 'split4pdf.pdf'))

        r = split4pdf(
            input_file=input_file,
            output_file=output_file,
            from_page=1,
            to_page=1,
        )
        logger.info(r)

        # 添加断言
        self.assertTrue(r)

    def test_split4pdfs(self):
        input_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'tests', 'test_files', 'pdf'))
        output_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'tests', 'test_files', 'pdf'))

        r = split4pdf(
            input_path=input_path,
            output_path=output_path,
            from_page=1,
            to_page=1,
        )
        logger.info(r)

        # 添加断言
        self.assertTrue(r)

