from pathlib import Path

from pofile import get_files, mkdir

from popdf.lib.utils import third_convert


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
