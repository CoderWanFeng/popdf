import os
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


# PDF解密
def pdf_to_decrypt(input_file=None, password=None, output_file=None):
    try:
        if input_file and password and output_file:
            # 创建一个PdfReader对象，并提供密码来解密PDF文件
            pdf_reader = PdfReader(input_file, password=password)
            # 创建一个PdfWriter对象
            pdf_writer = PdfWriter()

            # 逐页将解密后的PDF添加到新的PDF文件中
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
            os.makedirs(Path(output_file).parent,exist_ok=True)
            # 将解密后的PDF写入文件
            with open(output_file, 'wb') as out:
                pdf_writer.write(out)
        else:
            print("Please provide input file and password and output file")
    except Exception as e:
        raise e