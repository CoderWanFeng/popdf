# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pdf2word-cli',
    version='1.0.0',
    py_modules=['pdf2word'],
    install_requires=[
        'popdf',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'pdf2word=pdf2word:pdf2word',
        ],
    },
    author='PDF转换开发团队',
    description='PDF转Word命令行工具',
    python_requires='>=3.7',
)