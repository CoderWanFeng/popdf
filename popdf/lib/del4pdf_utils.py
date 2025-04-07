from pathlib import Path

import pymupdf
from loguru import logger


def del_page(page_nums, input_file=None, output_file=None):
    # 打开输入的 PDF 文件
    input_pdf = pymupdf.open(input_file)
    for page_num in page_nums:
        if page_num - 1 < 0:
            continue
        if page_num > input_pdf.page_count + 1:
            continue
        del input_pdf[page_num - 1]
        logger.info(f"{Path(input_file).name} del page :{page_num}")
    # # 将新文档保存到输出文件
    input_pdf.save(output_file)
    input_pdf.close()
