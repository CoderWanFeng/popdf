"""
popdf - PDF自动化处理工具库

一个功能强大的Python库，用于处理PDF文件的各种操作，包括：
- PDF转Word文档
- PDF转图片
- TXT转PDF
- PDF分割与合并
- PDF加密与解密
- 添加文本水印

安装方式：
    pip install popdf

快速入门：
    import popdf
    
    # PDF转Word
    popdf.pdf2docx(input_file='input.pdf', output_file='output.docx')
    
    # PDF转图片
    popdf.pdf2imgs(input_file='input.pdf', output_path='/images/')
    
    # PDF加密
    popdf.encrypt4pdf(password='secret', input_file='input.pdf', output_file='encrypted.pdf')

官方文档：https://www.python-office.com/office/pdf.html
GitHub: https://github.com/CoderWanFeng/popdf

版本信息：
"""
from popdf.api.pdf import *

__version__ = '1.0.8'
__author__ = '程序员晚枫'
__license__ = 'MIT'
__url__ = 'https://www.python-office.com/office/pdf.html'
__status__ = 'Production'
__description__ = 'PDF自动化处理库：转换、分割、合并、加密、水印'

__doc__ = """
popdf - PDF自动化处理工具库

功能列表：
---------
1. pdf2docx - PDF转Word
2. pdf2imgs - PDF转图片
3. txt2pdf - TXT转PDF
4. split4pdf - PDF分割
5. encrypt4pdf - PDF加密
6. decrypt4pdf - PDF解密
7. add_text_watermark - 添加文本水印
8. merge2pdf - PDF合并
9. del4pdf - 删除PDF页面

使用示例：
--------
>>> import popdf
>>> popdf.pdf2docx(input_file='document.pdf', output_file='document.docx')
"""

__all__ = [
    'pdf2docx',
    'pdf2imgs',
    'txt2pdf',
    'split4pdf',
    'encrypt4pdf',
    'decrypt4pdf',
    'add_text_watermark',
    'merge2pdf',
    'del4pdf',
]

__deprecated__ = [
    'add_watermark',
    'add_img_water',
    'add_watermark_by_parameters',
]