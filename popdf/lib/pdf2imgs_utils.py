# -*- coding: UTF-8 -*-
from pathlib import Path

import pymupdf  # PyMuPDF
from PIL import Image
from pofile import mkdir
from poprogress import simple_progress


def pdf_to_images(input_file, output_path):
    pdfDoc = pymupdf.open(input_file)
    page_count = pdfDoc.page_count
    for pg in simple_progress(range(pdfDoc.page_count)):
        print(f'processing page： {pg}/{page_count}')
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = pymupdf.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        mkdir(output_path)
        pdf_file_name = Path(input_file).stem
        pix.save(f'{str(Path(output_path).absolute())}/ {pdf_file_name}-{pg}.jpg')


def pdf_to_merge_image(input_file, output_file, dpi=300):
    """
    直接合并为1张图片
    """
    # 打开 PDF 文件
    pdf_document = pymupdf.open(input_file)
    images_list = []

    # 遍历 PDF 的每一页
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # 加载页面
        # 将页面转换为图片，设置 DPI 以提高清晰度
        pix = page.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72), alpha=False)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images_list.append(img)

    # 计算合并后的图片宽度（取最宽的图片宽度）和总高度
    widths, heights = zip(*(i.size for i in images_list))
    total_width = max(widths)
    total_height = sum(heights)

    # 创建一个新的空白图片，用于存放合并后的图片
    new_image = Image.new('RGB', (total_width, total_height))

    # 将每张图片按顺序粘贴到新的图片上
    y_offset = 0
    for img in images_list:
        # 调整图片大小以适应空白图片的宽度
        img = img.resize((total_width, int(img.height * (total_width / img.width))))
        new_image.paste(img, (0, y_offset))
        y_offset += img.height

    # 保存合并后的图片
    new_image.save(output_file)
