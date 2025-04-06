# -*- coding: utf-8 -*-

import sys


class PDFException(Exception):
    """tencentcloudapi sdk 异常类"""

    def __init__(self, code=None, message=None):
        self.code = code
        self.message = message

    def __str__(self):
        s = f"[TencentCloudSDKException] code:{self.code} message:{self.message}"
        if sys.version_info[0] < 3 and isinstance(s, unicode):
            return s.encode("utf8")
        else:
            return s

    def get_code(self):
        return self.code

    def get_message(self):
        return self.message
