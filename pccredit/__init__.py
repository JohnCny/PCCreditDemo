#!/usr/bin/env python
#coding=utf-8
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

from flask import Flask, render_template,flash

# 初始化
app = Flask(__name__)
app.config['DEBUG'] = True

# 路由
import views.index
# import views.khjlxxgl
