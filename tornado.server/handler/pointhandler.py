
import tornado.web
from tornado.options import options

import pymongo
from pymongo import MongoClient

import setting

from PIL import Image
import io
import os.path

import json

import subprocess

import pandas as ps
import math
import glob

import pandas as ps

g_DF = ps.read_csv('./imglib/labellist.csv');
g_liLabeledImg = list(g_DF['name'])
g_LabelFile = open('./imglib/labellist.csv', 'a')

class TestHandler(tornado.web.RequestHandler):
    def get(self, word):
        print('getsurvey handler', word);       
        self.write('ok');


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class SaveHandler(tornado.web.RequestHandler):
	def post(self):
		self.set_header('Access-Control-Allow-Origin', '*')
		print(self.get_argument('name'))
		fileName = self.get_argument('name')
		liLabel = json.loads(self.get_argument('labels'));
		labelFile = open('./imglib/labels/' + fileName.split('.')[0] + '.txt', 'w')
		if((fileName in g_liLabeledImg) == False):
			print('labeled')
			g_LabelFile.write(fileName + '\n')
		for label in liLabel:
			print(str(label[0]) + ','  + str(label[1]) + ',' + str(label[2]) 
				+ ',' + str(label[3]) + ',' + str(label[4]))
			labelFile.write(str(label[0]) + ','  + str(label[1]) + ',' + str(label[2]) 
				+ ',' + str(label[3]) + ',' + str(label[4]) + '\n')
		labelFile.close();
		print('ok')
		self.write({'ok': 'yes'});

class ImgHandler(tornado.web.RequestHandler):
	def get(self):
		print('get imgs')
		self.write('ok')

	def post(self):

		print('get imgs', self.static_url('./imglib/info.csv'))

		imgList = glob.glob("./imglib/*.jpg")

		# df_img = ps.read_csv('./imglib/labeled.csv')
		# imgList = list(df_img['name'])
		# print('img list', imgList[0: 5], len(imgList))
		x = []
		# reader = 0
		for img in imgList:
   			imgName = basename(img)
   			x.append(imgName)
			# if(reader >= 320 and reader < 330):
			# if(type(img) == float and math.isnan(img)):
			# 	print(img, type(img))
			# 	continue
			# print(img, type(img))
			# reader += 1
			
		self.set_header('Access-Control-Allow-Origin', '*')
		self.write({'imgList': x})

