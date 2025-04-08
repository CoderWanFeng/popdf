import os
from pathlib import Path

import pymupdf
from pofile import get_files, mkdir
from poprogress import simple_progress

from popdf.lib.del4pdf_utils import del_page
from popdf.lib.pdf2docx_utils import third_convert
from popdf.lib.pdf2imgs_utils import pdf_to_images, pdf_to_merge_image
from popdf.lib.pdfdecrypt_utils import pdf_to_decrypt


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

    # 批量pdf解密
    # 暂时不支持递归文件夹下的目录
    def pdf2decryptBatch(self, input_path=None, output_path=None ,password=None):
        if input_path and output_path and password:
            try:
                for file in os.listdir(input_path):
                    file_path = os.path.join(input_path, file)
                    output_file = os.path.join(output_path, file)
                    if os.path.isfile(file_path) and file.endswith(".pdf"):
                        pdf_to_decrypt(input_file=file_path, password=password, output_file=output_file)
                    else:
                        print('skip %s' % file)
            except Exception as e:
                print(e)
        else:
            print("Please provide input path and password and output path")

    def pdf2imgs(self, input_path: str, output_path=None, merge: bool = False) -> None:
        if output_path:
            mkdir(Path(output_path))
        pdf_files = get_files(path=input_path, suffix=self.pdf_suffix)
        if merge:
            for pdf_file in simple_progress(pdf_files):
                pdf_to_merge_image(input_file=pdf_file,
                                   output_file=Path(output_path) / str(Path(pdf_file).stem) + '.jpg')
        else:
            for pdf_file in simple_progress(pdf_files):
                pdf_to_images(input_file=pdf_file, output_path=Path(output_path) / Path(pdf_file).stem)

    def txt2pdf(self, input_path=None, output_path=None):
        txt_files = get_files(path=input_path, suffix='.txt')
        mkdir(Path(output_path))
        for input_file in txt_files:
            # https://pymupdf.readthedocs.io/en/latest/recipes-common-issues-and-their-solutions.html#how-to-convert-any-document-to-pdf
            if not (list(map(int, pymupdf.VersionBind.split("."))) >= [1, 14, 0]):
                raise SystemExit("need PyMuPDF v1.14.0+")
            output_file = Path(output_path) / str(Path(input_file).stem + '.pdf')
            print("Converting '%s' to '%s.pdf'" % (input_file, output_file))

            doc = pymupdf.open(input_file)

            b = doc.convert_to_pdf()  # convert to pdf
            pdf = pymupdf.open("pdf", b)  # open as pdf

            toc = doc.get_toc()  # table of contents of input
            pdf.set_toc(toc)  # simply set it for output
            meta = doc.metadata  # read and set metadata
            if not meta["producer"]:
                meta["producer"] = "PyMuPDF v" + pymupdf.VersionBind

            if not meta["creator"]:
                meta["creator"] = "PyMuPDF PDF converter"
            meta["modDate"] = pymupdf.get_pdf_now()
            meta["creationDate"] = meta["modDate"]
            pdf.set_metadata(meta)

            # now process the links
            link_cnti = 0
            link_skip = 0
            for pinput in doc:  # iterate through input pages
                links = pinput.get_links()  # get list of links
                link_cnti += len(links)  # count how many
                pout = pdf[pinput.number]  # read corresp. output page
                for l in links:  # iterate though the links
                    if l["kind"] == pymupdf.LINK_NAMED:  # we do not handle named links
                        print("named link page", pinput.number, l)
                        link_skip += 1  # count them
                        continue
                    pout.insert_link(l)  # simply output the others
            mkdir(Path(output_file).parent)
            # save the conversion result
            pdf.save(output_file, garbage=4, deflate=True)
            # say how many named links we skipped
            if link_cnti > 0:
                print("Skipped %i named links of a total of %i in input." % (link_skip, link_cnti))

    # 删除指定页面
    def del4pdf(self, page_nums, input_path=None, output_path=None):
        """
        使用 pymupdf 从 PDF 文件中删除指定的页面。

        参数:
        input_file (str): 输入的 PDF 文件路径。
        page_nums (list): 需要删除的页面编号列表（基于0索引，注意页面编号不连续）。
        output_file (str): 输出（修改后）的 PDF 文件路径。
        """
        pdf_files = get_files(path=input_path, suffix=self.pdf_suffix)
        mkdir(Path(output_path))
        for input_file in pdf_files:
            output_file = Path(output_path) / Path(input_file).name
            del_page(page_nums, input_file, output_file)
