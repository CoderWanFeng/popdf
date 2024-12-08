import unittest

from popdf.api.pdf import *


class TestPDF(unittest.TestCase):

    def test_add_text_watermark(self):
        add_text_watermark(input_file=r'./test_files/pdf/merge.pdf', point=(50, 50),
                           output_file=r'./test_files/pdf/add_text_watermark.pdf')

    def test_txt2pdf(self):
        # 准备测试数据
        input_file = "test.txt"
        output_file = "./test_files/pdf/test.pdf"

        # 写入测试文本
        with open(input_file, 'w') as f:
            f.write("This is a test text.")
        # 调用被测方法
        txt2pdf(input_file, output_file)

    def test_pdf2docx(self):
        pdf2docx(
            input_file=r'test_files/pdf/merge.pdf',
            output_path=r'./test_files/docx/'
        )

    def test_merge2pdf(self):
        merge2pdf(
            input_file_list=[r'./test_files/pdf/merge.pdf', r'./test_files/pdf/merge.pdf'],
            output_file=r'./test_files/pdf/merge2pdf.pdf'
        )

    def test_encrypt4pdf(self):
        encrypt4pdf(
            input_file=r'./test_files/pdf/merge.pdf',
            password='123456',
            output_file=r'./test_files/pdf/encrypt4pdf.pdf'
        )

    def test_decrypt4pdf(self):
        decrypt4pdf(
            input_file=r'./test_files/pdf/encrypt4pdf.pdf',
            password='123456',
            output_file=r'./test_files/pdf/decrypt4pdf.pdf'
        )

    def test_pdf2imgs(self):
        pdf2imgs(
            input_file=r'test_files/pdf/merge.pdf',
            output_path='./test_files/img/')

    def test_split4pdf(self):
        split4pdf(
            input_file=r'./test_files/pdf/merge.pdf',
            from_page=1,
            output_file=r'./test_files/pdf/split4pdf.pdf'
        )

    ##############  以下方法待优化  #################

    def test_pdf2imgs_merge(self):
        pdf2imgs(
            input_file=r'test_files/pdf/merge.pdf',
            output_path=r'./test_files/img/merge',
            merge=True
        )

    ##############  以下方法未测试  #################
    def test_add_img_water(self):
        add_img_water(pdf_file_in='./test_files/pdf/add_img.pdf', pdf_file_mark='test_files/pdf/merge.pdf',
                      pdf_file_out='add_img_res.pdf')

    def test_add_watermark_by_parameters(self):
        add_watermark_by_parameters(
            pdf_file=r'/tests/test_files/pdf/merge.pdf',
            mark_str='python-office',
            output_path=None,
            output_file_name=None)

    def test_add_watermark(self):
        stub_stdin(self, './test_files/pdf/merge.pdf\npython-office\n')  # 依次输入
        add_watermark()
