from pathlib import Path

from loguru import logger
from pdf2docx import Converter


def third_convert(pdf_file, word_file):
    pdf_file = Path(pdf_file).absolute()
    if not pdf_file.exists():
        logger.error(f"{pdf_file} does not exist")
        return 0
    if not pdf_file.suffix == ".pdf":
        logger.error(f"{pdf_file} is not a pdf file")
        return 0
    word_file = Path(word_file).absolute()
    if not word_file.suffix == ".docx":
        logger.error(f"{word_file} is not a docx file")
        return 0
    logger.info(f"Converting {pdf_file} to {word_file}")
    cv = Converter(pdf_file)
    cv.convert(word_file)
    cv.close()
