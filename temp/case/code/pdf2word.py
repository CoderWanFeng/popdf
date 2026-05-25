# -*- coding: utf-8 -*-
# 这行告诉 Python 这个文件使用 UTF-8 编码，可以支持中文

# 导入 popdf 库，这是一个用于处理 PDF 文件的工具库
import popdf

# 调用 popdf 库中的 pdf2docx 函数来转换 PDF 到 Word
popdf.pdf2docx(
    # input_file: 你要转换的 PDF 文件路径（需要改成你自己的文件路径）
    input_file=r'/path/to/input.pdf',
    # output_file: 转换后生成的 Word 文件路径（需要改成你想要保存的位置）
    output_file=r'/path/to/output.docx'
)
