# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/12/6 21:45 
@本段代码的视频说明     ：
'''
import pymupdf  # PyMuPDF


def add_watermark_to_pdf(pdf_path, output_path, watermark_image_path):
    # 打开PDF文件
    doc = pymupdf.open(pdf_path)

    # 遍历PDF的每一页
    for page in doc:
        width, height = page.mediabox.width, page.mediabox.height

        # 定义水印的位置和大小
        rect = pymupdf.Rect(width - 50, 0, width, height)  # 在页面右下角添加水印

        # 插入水印图片
        page.insert_image(rect, filename=watermark_image_path, overlay=True)

    # 保存修改后的PDF文件
    doc.save(output_path)

    # 关闭PDF文件
    doc.close()


if __name__ == '__main__':
    # 使用示例
    pdf_path = 'example.pdf'  # 输入PDF文件路径
    output_path = 'output_with_watermark.pdf'  # 输出PDF文件路径
    watermark_image_path = 'watermark.png'  # 水印图片路径

    add_watermark_to_pdf(pdf_path, output_path, watermark_image_path)
