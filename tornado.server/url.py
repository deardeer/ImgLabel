#!/usr/bin/env python
#coding:utf-8

import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')

from handler.pointhandler import IndexHandler
from handler.pointhandler import TestHandler
from handler.pointhandler import ImgHandler
from handler.pointhandler import SaveHandler

url=[
	(r'/', IndexHandler),
    # (r'/test/(\w+)', TestHandler),
    (r'/getImgList', ImgHandler),
    (r'/save', SaveHandler),
]