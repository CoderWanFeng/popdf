# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/12/8 18:25 
@本段代码的视频说明     ：
'''
# import pymupdf
#
test_file = r'test_files/merge.pdf'
#
# # 打开PDF文件
# doc = pymupdf.open(test_file)
#
# # 遍历PDF的每一页
# for page in doc:
#
#     page.add_stamp_annot(pymupdf.Rect(50, 50, 200, 100), 5)
#
#     # 保存PDF文件
#     doc.save("watermarked_document.pdf")

import pymupdf  # PyMuPDF


def add_watermark_to_pdf(input_path, point, text, watermark_text='程序员晚枫',
                         output_path='./pdf_watermark.pdf', fontname="Helvetica", fontsize=12, color=(1, 0, 0), ):
    # 打开输入PDF文件
    doc = pymupdf.open(input_path)

    # 遍历PDF的每一页
    for page in doc:
        # 插入文本
        page.insert_text(point=point, text=text, fontname=fontname, fontsize=fontsize, color=color)

    # 保存修改后的PDF文件
    doc.save(output_path)
    doc.close()  # 关闭PDF文件


# 调用函数添加水印
add_watermark_to_pdf(test_file, '程序员晚枫', 'output_with_watermark.pdf')
