import pymupdf

from pathlib import Path
from pofile import mkdir


def split_for_pdf(input_file, output_file, from_page, to_page):
    # 因为Python从0开始计数，所以需要减1
    from_page -= 1
    to_page -= 1
    # 打开输入原始PDF文件
    pdf_document = pymupdf.open(input_file)

    mkdir(Path(output_file).parent)

    # 创建一个新的PDF文档
    pdf_document_new = pymupdf.open()

    pdf_document_new.insert_pdf(pdf_document, from_page=from_page, to_page=to_page)

    # 保存分割后的PDF文件
    pdf_document_new.save(output_file)

    # 关闭文件
    pdf_document.close()
    pdf_document_new.close()
