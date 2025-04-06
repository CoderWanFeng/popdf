from pathlib import Path

from pofile import get_files, mkdir
from poprogress import simple_progress

from popdf.lib.pdf2docx_utils import third_convert
from popdf.lib.pdf2imgs_utils import pdf_to_images, pdf_to_merge_image


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

    def pdf2imgs(self, input_path: str, output_path=None, merge: bool = False) -> None:
        if output_path:
            mkdir(Path(output_path))
        pdf_files = get_files(path=input_path, suffix=self.pdf_suffix)
        if merge:
            for pdf_file in simple_progress(pdf_files):
                pdf_to_merge_image(input_file=pdf_file, output_file=str(Path(output_path) / Path(pdf_file).stem) + '.jpg')
        else:
            for pdf_file in simple_progress(pdf_files):
                pdf_to_images(input_file=pdf_file, output_path=Path(output_path) / Path(pdf_file).stem)

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
