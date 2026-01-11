import os
import unittest
from pathlib import Path

from popdf.api.pdf import *
from popdf.api.pdf import split4pdf


class TestPDF(unittest.TestCase):
    """PDF功能测试套件 - 使用统一测试文件和输出目录"""
    
    @classmethod
    def setUpClass(cls):
        """设置测试环境"""
        cls.base_dir = Path(__file__).resolve().parent
        cls.input_pdf = cls.base_dir / '..' / 'test_files' / 'pdf' / '程序员晚枫.pdf'
        cls.output_dir = cls.base_dir / '..' / 'test_files' / 'test_out'
        
        # 确保输出目录存在
        cls.output_dir.mkdir(parents=True, exist_ok=True)

    def test_pdf2docx(self):
        """
        测试PDF转Word功能
        """
        func_output_dir = self.output_dir / 'pdf2docx'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        output_file = func_output_dir / '程序员晚枫.docx'
        pdf2docx(
            input_file=self.input_pdf,
            output_file=output_file
        )
        self.assertTrue(output_file.exists())

    def test_pdf2imgs(self):
        """
        测试PDF转图片功能
        """
        func_output_dir = self.output_dir / 'pdf2imgs'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        output_dir = func_output_dir / 'imgs'
        pdf2imgs(
            input_file=self.input_pdf,
            output_file=output_dir
        )
        self.assertTrue(output_dir.exists())

    def test_pdf2imgs_merge(self):
        """
        测试PDF转合并图片功能
        """
        func_output_dir = self.output_dir / 'pdf2imgs_merge'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        output_file = func_output_dir / 'merged_image.jpg'
        pdf2imgs(
            input_file=self.input_pdf,
            output_file=output_file,
            merge=True
        )
        self.assertTrue(output_file.exists())

    def test_txt2pdf(self):
        """
        测试文本转PDF功能
        """
        func_output_dir = self.output_dir / 'txt2pdf'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        # 创建临时文本文件
        input_txt = func_output_dir / 'test_input.txt'
        with open(input_txt, 'w', encoding='utf-8') as f:
            f.write('这是一个测试文本\n')
            f.write('用于测试txt2pdf功能\n')
            f.write('程序员晚枫 - Python-Office')
        
        output_file = func_output_dir / 'txt2pdf.pdf'
        txt2pdf(input_file=input_txt, output_file=output_file)
        self.assertTrue(output_file.exists())

    def test_split4pdf(self):
        """
        测试PDF分割功能
        """
        func_output_dir = self.output_dir / 'split4pdf'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        output_file = func_output_dir / 'split4pdf.pdf'
        split4pdf(
            input_file=self.input_pdf,
            from_page=1,
            to_page=2,
            output_file=output_file
        )
        self.assertTrue(output_file.exists())

    def test_encrypt4pdf(self):
        """
        测试PDF加密功能
        """
        func_output_dir = self.output_dir / 'encrypt4pdf'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        output_file = func_output_dir / 'encrypt4pdf.pdf'
        encrypt4pdf(
            input_file=self.input_pdf,
            password='123456',
            output_file=output_file
        )
        self.assertTrue(output_file.exists())

    def test_decrypt4pdf(self):
        """
        测试PDF解密功能
        """
        func_output_dir = self.output_dir / 'decrypt4pdf'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        # 先加密一个PDF
        encrypted_file = func_output_dir / 'encrypted_temp.pdf'
        encrypt4pdf(
            input_file=self.input_pdf,
            password='123456',
            output_file=encrypted_file
        )
        
        # 再解密
        output_file = func_output_dir / 'decrypt4pdf.pdf'
        decrypt4pdf(
            input_file=encrypted_file,
            password='123456',
            output_file=output_file
        )
        self.assertTrue(output_file.exists())

    def test_add_text_watermark(self):
        """
        测试添加文本水印功能
        """
        func_output_dir = self.output_dir / 'add_text_watermark'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        output_file = func_output_dir / 'watermark.pdf'
        add_text_watermark(
            input_file=self.input_pdf,
            point=(297, 421),  # A4页面尺寸约595x842点，中心位置约(297, 421)
            text='白开水AI社区',
            output_file=output_file,
            fontname='china-s',
            fontsize=48
        )
        self.assertTrue(output_file.exists())

    def test_merge2pdf(self):
        """
        测试PDF合并功能
        """
        func_output_dir = self.output_dir / 'merge2pdf'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        # 先创建两个分割后的PDF文件
        pdf1 = func_output_dir / 'merge_part1.pdf'
        pdf2 = func_output_dir / 'merge_part2.pdf'
        
        split4pdf(input_file=self.input_pdf, from_page=1, to_page=1, output_file=pdf1)
        split4pdf(input_file=self.input_pdf, from_page=2, to_page=2, output_file=pdf2)
        
        output_file = func_output_dir / 'merge2pdf.pdf'
        merge2pdf(
            input_file_list=[pdf1, pdf2],
            output_file=output_file
        )
        self.assertTrue(output_file.exists())

    def test_del4pdf(self):
        """
        测试删除PDF页面功能
        """
        func_output_dir = self.output_dir / 'del4pdf'
        func_output_dir.mkdir(parents=True, exist_ok=True)
        output_file = func_output_dir / 'del4pdf.pdf'
        del4pdf(
            input_file=self.input_pdf,
            page_nums=[1],  # 删除第1页
            output_file=output_file
        )
        self.assertTrue(output_file.exists())


# 当前脚本所在目录
base_dir = Path(__file__).resolve().parent
