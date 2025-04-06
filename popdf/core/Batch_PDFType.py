from pathlib import Path

from pofile import get_files, mkdir

from popdf.lib.pdf2docx_utils import third_convert


class Batch_PDFType():
    def __init__(self):
        self.pdf_suffix = '.pdf'
        self.docx_suffix = '.docx'

    def pdf2docx(self, input_path=None, output_path=None):
        if input_path and output_path:
            mkdir(Path(output_path))
            waiting_convert_pdf_files = get_files(path=input_path, suffix=self.pdf_suffix)
            if waiting_convert_pdf_files:
                for pdf_file in waiting_convert_pdf_files:
                    pdf_file = Path(pdf_file).absolute()
                    word_name = pdf_file.stem + self.docx_suffix
                    word_path = Path(output_path) / word_name
                    third_convert(pdf_file, word_path)

    def pdf2imgs(self, input_file: str, output_path="./", merge: bool = False) -> None:
        pdf_file_list = get_files(input_file, suffix='.pdf')
        for pdf_file in simple_progress(pdf_file_list):
            pdfDoc = pymupdf.open(pdf_file)
            page_count = pdfDoc.page_count
            for pg in simple_progress(range(pdfDoc.page_count)):
                print(f'正在处理第{pg}/{page_count}页')
                page = pdfDoc[pg]
                rotate = int(0)
                # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
                # 此处若是不做设置，默认图片大小为：792X612, dpi=96
                zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
                zoom_y = 1.33333333
                mat = pymupdf.Matrix(zoom_x, zoom_y).prerotate(rotate)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                mkdir(output_path)
                pdf_file_name = Path(pdf_file).stem
                pix.save(output_path + f'/ {pdf_file_name}-{pg}.jpg')  # 将图片写入指定的文件夹内

        print(f'PDF转换Image完成，图片在你指定的output文件夹{output_path}，如果没有指定，默认是PDF同一个文件夹')
        if merge:
            """
            TODO：目前的问题：多个PDF批量转换后的图片，会合成在一张图里
            """
            self.generate_long_image(input_path=output_path,
                                     output_path=os.path.join(output_path, "merge_output"),
                                     img_name=pdf_file_name + '.jpg')

    def generate_long_image(self, input_path: str, output_path, img_name='merge.jpg'):
        """
        将ppt的各个页面拼接成长图：https://blog.csdn.net/m0_51777056/article/details/130262561
        :param input_path:
        :param output_path:
        :param img_name:
        :return:
        """
        # 获取图片列表
        img_list = []
        for imgs in os.listdir(input_path):
            img_list.append(os.path.join(input_path, imgs))

        # 将获取到ppt的页面进行排序
        ims_sort = sorted(img_list, key=lambda jpg: len(jpg))

        width, height = Image.open(img_list[0]).size  # 取第一个图片尺寸
        img_mode = Image.open(img_list[0]).mode
        long_canvas = Image.new(img_mode, (width, height * len(img_list)))  # 创建同宽，n倍高的空白图片

        # 拼接图片
        for i, image in enumerate(ims_sort):
            long_canvas.paste(Image.open(image), box=(0, i * height))
        mkdir(output_path)
        long_canvas.save(os.path.join(output_path, img_name))  # 保存长图
