import pymupdf

from pathlib import Path
from pofile import mkdir
from loguru import logger


def split_for_pdf(input_file, output_file, from_page, to_page):
    # 因为Python从0开始计数，所以需要减1
    from_page -= 1
    if to_page != -1:
        to_page -= 1

    if from_page < 0:
        logger.error("from_page不能小于1")
        return

    # 打开输入原始PDF文件
    pdf_document = pymupdf.open(input_file)

    if to_page + 1 > pdf_document.page_count:
        logger.error(f"to_page不能大于PDF总页数，总页数为{pdf_document.page_count}")
        return

    mkdir(Path(output_file).parent)

    # 创建一个新的PDF文档
    pdf_document_new = pymupdf.open()

    pdf_document_new.insert_pdf(pdf_document, from_page=from_page, to_page=to_page)

    # 保存分割后的PDF文件
    pdf_document_new.save(output_file)

    # 关闭文件
    pdf_document.close()
    pdf_document_new.close()
