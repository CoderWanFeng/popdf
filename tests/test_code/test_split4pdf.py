import unittest

from popdf.api.pdf import split4pdf

from loguru import logger

class TestOCR(unittest.TestCase):
    """
    pdf.py测试用的代码
    """
    def test_split4pdf(self):
        input_file = r'E:\popdf\tests\test_files\pdf\程序员晚枫.pdf'
        output_file = r'E:\popdf\tests\test_files\pdf\split4pdf.pdf'

        r = split4pdf(
            input_file=input_file,
            output_file=output_file,
            from_page=1,
            to_page=1,
        )
        logger.info(r)

    def test_split4pdfs(self):
        input_path = r'E:\popdf\tests\test_files\pdf'
        output_path = r'E:\popdf\tests\test_files\pdf'

        r = split4pdf(
            input_path=input_path,
            output_path=output_path,
            from_page=1,
            to_page=1,
        )
        logger.info(r)


if __name__ == '__main__':
    unittest.main()
