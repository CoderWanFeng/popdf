# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2025/4/5 23:46 
@本段代码的视频说明     ：
'''

import fitz  # PyMuPDF
from PIL import Image


def pdf_to_long_image(pdf_path, output_path, dpi=300):
    # 打开 PDF 文件
    pdf_document = fitz.open(pdf_path)
    images_list = []

    # 遍历 PDF 的每一页
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # 加载页面
        # 将页面转换为图片，设置 DPI 以提高清晰度
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), alpha=False)
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
    new_image.save(output_path)


# 使用示例
pdf_file = r'D:\workplace\code\gitcode\popdf\tests\test_files\pdf2imgs\程序员晚枫.pdf'  # 替换为你的 PDF 文件路径
output_image = 'output_image.jpg'  # 替换为你想要保存的图片路径
pdf_to_long_image(pdf_file, output_image)
