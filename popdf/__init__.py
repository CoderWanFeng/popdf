from popdf.api.pdf import *

__version__ = '1.0.7'
__author__ = '程序员晚枫'
__license__ = 'MIT'
__url__ = 'https://www.python-office.com/office/pdf.html'
__status__ = 'Production'
__description__ = 'PDF自动化处理库：转换、分割、合并、加密、水印'

__doc__ = "popdf docs:https://www.python-office.com/office/pdf.html"

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
    'add_watermark',
    'add_img_water',
    'add_watermark_by_parameters',
]

__deprecated__ = [
    'add_watermark',
    'add_img_water',
    'add_watermark_by_parameters',
]
