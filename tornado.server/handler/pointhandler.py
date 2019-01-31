
import tornado.web
from tornado.options import options

import pymongo
from pymongo import MongoClient
from os.path import basename

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

# g_DF = ps.read_csv('./imglib/labellist.csv');
# g_liLabeledImg = list(g_DF['name'])
# g_LabelFile = open('./imglib/labellist.csv', 'a')

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
		labelFile = open('./imglib/' + fileName.split('.')[0] + '.txt', 'w')
		print('Save Label ', './imglib/' + fileName.split('.')[0] + '.txt')
		conStr = ' '
		for label in liLabel:
			print(str(label[0]) + conStr + str(label[1]) + conStr + str(label[2]) 
				+ conStr + str(label[3]) + conStr + str(label[4]) + conStr + str(label[5]))
			labelFile.write(str(label[0]) + conStr  + str(label[1]) + conStr + str(label[2]) 
				+ conStr + str(label[3]) + conStr + str(label[4]) + conStr + str(label[5]) + '\n')
		labelFile.close();
		print('ok')
		self.write({'ok': 'yes'});


class GetHandler(tornado.web.RequestHandler):
	def post(self):
		self.set_header('Access-Control-Allow-Origin', '*')
		print(self.get_argument('name'))
		fileName = self.get_argument('name')		
		labelFile = open('./imglib/' + fileName.split('.')[0] + '.txt', 'r')
		liLabel = []
		for line_of_text in labelFile:
			if(line_of_text != '\n'):
				labelType = line_of_text.split(' ')[0]
				label = line_of_text.split(' ')[1]
				labelInfo = [int(label)]
				xywh = [float(x) for x in line_of_text.split(' ')[2:]]
				labelInfo += xywh
				liLabel.append([labelType, label])
				print('label', label, labelInfo, 'xywh', xywh, type(xywh), len(xywh), line_of_text.split(' '))
				# mapLabelInfo = [int(label), xywh]
		print('line_of_text', liLabel)
		labelFile.close();
		print('ok')
		self.write({'labels': liLabel});

class ImgHandler(tornado.web.RequestHandler):

	def get(self):
		print('get imgs')
		self.write('ok')

	def post(self):

		# print('get imgs', self.static_url('./imglib/info.csv'))

		imgList = glob.glob("./imglib/*.jpg")

		# df_img = ps.read_csv('./imglib/labeled.csv')
		# imgList = list(df_img['name'])
		x = {}
		# x.push('./imglib/002834.jpg')
		
		# reader = 0
		for img in imgList:
   			imgName = basename(img).split('.')[0]
   			x[imgName] = img
		
		labelList = glob.glob('./imglib/*.txt')

		print('img list', imgList[0: 5], len(imgList))

		y = {}
		# y.push('./imglabel/002834.txt')

		for fileDir in labelList:
   			fileName = basename(fileDir).split('.')[0]
   			y[fileName] = fileDir
		
			
		self.set_header('Access-Control-Allow-Origin', '*')
		self.write({'img': x, 'label': y})

