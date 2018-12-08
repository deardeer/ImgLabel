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
from handler.pointhandler import GetHandler

url=[
	(r'/', IndexHandler),
    # (r'/test/(\w+)', TestHandler),
    (r'/getImgList', ImgHandler),
    (r'/save', SaveHandler),
    (r'/get', GetHandler),
]