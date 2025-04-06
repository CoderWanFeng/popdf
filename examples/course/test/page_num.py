import fitz  # 导入Fitz库

font = fitz.Font("cjk")


def add_page_numbers(input_pdf, output_pdf):
    # 打开输入PDF文件
    pdf_document = fitz.open(input_pdf)
    # 获取总页数
    total_pages = len(pdf_document)
    for page_num in range(total_pages):
        page = pdf_document[page_num]
        # 设置页码文本
        page_number_text = f"{page_num + 1} / {total_pages} "
        # 页面的宽度和高度
        width = page.rect.width
        height = page.rect.height
        print(width, height)
        page.insert_font(fontname="F0", fontbuffer=font.buffer)
        # pos = fitz.Point(width / 2 - 10, height - 30)  # 页面底部中间
        pos = fitz.Point(width - 80, height - 20)  # 页面底部右侧
        # 设置字体（这里使用Helvetica）和大小
        page.insert_text(pos, page_number_text, fontsize=12)

    # 保存到输出PDF文件
    pdf_document.save(output_pdf)
    pdf_document.close()


# 使用示例
input_pdf_path = r"../code/test_files/pdf/程序员晚枫.pdf"
output_pdf_path = r"../code/test_files/pdf/t-1.pdf"
add_page_numbers(input_pdf_path, output_pdf_path)
