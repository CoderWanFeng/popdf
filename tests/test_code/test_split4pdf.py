import unittest

from popdf.api.pdf import split4pdf

from loguru import logger
import os
import popdf

# 当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

class TestOCR(unittest.TestCase):
    """
    pdf.py测试用的代码
    """
    def test_split4pdf(self):
        input_file = os.path.abspath(os.path.join(base_dir, '..', '..', 'tests', 'test_files', 'pdf', '程序员晚枫.pdf'))
        output_file = os.path.abspath(os.path.join(base_dir, '..', '..', 'tests', 'test_files', 'pdf', 'split4pdf.pdf'))

        r = split4pdf(
            input_file=input_file,
            output_file=output_file,
            from_page=1,
            to_page=1,
        )
        logger.info(r)

        # 添加断言
        self.assertTrue(r)

    def test_split4pdfs(self):
        input_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'tests', 'test_files', 'pdf'))
        output_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'tests', 'test_files', 'pdf'))

        r = split4pdf(
            input_path=input_path,
            output_path=output_path,
            from_page=1,
            to_page=1,
        )
        logger.info(r)

        # 添加断言
        self.assertTrue(r)

if __name__ == '__main__':
    unittest.main()
