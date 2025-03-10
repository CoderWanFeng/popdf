import PyPDF2
from PyPDF2 import PdfWriter, PdfReader


def encrypt_pdf(input_pdf_path, output_pdf_path, password):
    with open(input_pdf_path, 'rb') as file:
        reader = PdfReader(file)

        # 创建一个PdfFileWriter对象
        writer = PdfWriter()

        # 将每一页加入到writer中
        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])


        # 加密PDF
        writer.encrypt(password)

        # 写入加密后的PDF
        with open(output_pdf_path, 'wb') as out:
            writer.write(out)


def decrypt_pdf(input_pdf_path, output_pdf_path, password):
    pass


if __name__ == '__main__':

    e='encrypted_output.pdf'
    d='decrypted_output.pdf'
    # 使用示例
    # encrypt_pdf(r'./test_files/pdf/程序员晚枫.pdf', e, '123456')
    # 使用示例
    # decrypt_pdf(e, d, '123456')
    # https://blog.csdn.net/sinat_15136141/article/details/112135649
    # https://blog.csdn.net/sinat_15136141/article/details/112135649
    file_path= r'./test_files/pdf/程序员晚枫.pdf'
    # 打开PDF文件
    with open(file_path, 'rb') as file:
        # 创建一个PdfFileReader对象
        reader = PyPDF2.PdfFileReader(file)
